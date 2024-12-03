from flask import Flask, render_template, request, redirect, url_for, session, flash
from service.ProductService import ProductService
from service.UserService import UserService
from functools import wraps
from flask import redirect, url_for, flash, session


app = Flask(__name__)
app.secret_key = "your_secret_key"
product_service = ProductService()
user_service = UserService()

# _____________________________ ROUTES _____________________________ #

# Home Route
@app.route('/')
def home():
    products = product_service.get_all_products()
    return render_template('index.html', products=products)

# Product Routes
@app.route('/products')
def show_products():
    products = product_service.get_all_products()
    return render_template('ProductSpread.html', products=products)

@app.route('/products/<int:product_id>')
def show_product(product_id):
    product = product_service.get_product_details(product_id)
    if product:
        return render_template('individualProduct.html', product=product)
    else:
        flash('Product not found.')
        return redirect(url_for('show_products'))

# Login Route
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user_type = request.form['user_type']  # Get the selected user type

        # Authenticate user
        user = user_service.authenticate_user(email, password)
        if user:
            # Validate the user type matches the selected option
            if user.role == user_type:
                session['user_id'] = user.userid
                session['user_role'] = user.role
                session['user_firstname'] = user.firstname
                flash(f'Welcome back {user.firstname}! You are now logged in as a {user.role}.', 'success')
                return redirect(url_for('admin_dashboard' if user.role == 'admin' else 'home'))
            else:
                flash('Incorrect user type selected.', 'danger')
        else:
            flash("Invalid credentials. Please try again.", 'danger')

    return render_template('login.html')

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:  # Check if user is logged in
            flash('You must be logged in to complete this action.', 'warning')
            return redirect(url_for('login'))  # Redirect to login page
        return f(*args, **kwargs)
    return decorated_function

@app.route('/logout')
def logout():
    session.clear()  # Clear all session data
    flash('You have been logged out.', 'success')
    return redirect(url_for('login'))  # Redirect to login page


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Get form data
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']

        # Check if user already exists
        if user_service.get_user_by_email(email):
            flash('An account with this email already exists.', 'danger')
            return redirect(url_for('signup'))

        # Add new user
        user_service.create_user(firstname, lastname, email, password)
        flash('Account created successfully! You can now log in.', 'success')
        return redirect(url_for('login'))

    return render_template('signup.html')

# _____________________________ ADMIN ROUTES _____________________________ #

# Admin Dashboard
@app.route('/admin')
def admin_dashboard():
    if 'user_role' in session and session['user_role'] == 'admin':
        return render_template('admin_dashboard.html')
    else:
        flash("You do not have permission to access this page.")
        return redirect(url_for('login'))


@app.route('/admin/manage_users')
def manage_users():
    if 'user_role' in session and session['user_role'] == 'admin':
        users = user_service.get_all_users()
        return render_template('manage_users.html', users=users)
    else:
        flash("You do not have permission to access this page.")
        return redirect(url_for('login'))


@app.route('/admin/manage_products')
def manage_products():
    if 'user_role' in session and session['user_role'] == 'admin':
        products = product_service.get_all_products()
        return render_template('manage_products.html', products=products)
    else:
        flash("You do not have permission to access this page.")
        return redirect(url_for('login'))


@app.route('/admin/view_reports')
def view_reports():
    if 'user_role' in session and session['user_role'] == 'admin':
        # Dummy content for reports, can be expanded to real reporting data
        return render_template('view_reports.html')
    else:
        flash("You do not have permission to access this page.")
        return redirect(url_for('login'))

# _____________________________ CART ROUTES _____________________________ #

@app.route('/add_to_cart/<int:product_id>')
@login_required
def add_to_cart(product_id):
    cart = session.setdefault('cart', [])
    cart.append(product_id)
    session['cart'] = cart
    flash(f'Product {product_id} added to cart!', 'success')
    return redirect(url_for('show_products'))

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    discount_message = None
    discount_valid = False
    discount_applied = False
    discount_amount = 0.00

    if request.method == 'POST':
        # Handle delivery option
        if 'delivery_option' in request.form:
            session['delivery_cost'] = float(request.form.get('delivery_option', 0.00))
        # Handle discount code
        elif 'discount_code' in request.form:
            discount_code = request.form['discount_code']
            if discount_code.upper() == "SNEAKERSALE":  # Case-insensitive check for discount code
                discount_valid = True
                discount_message = "Discount code applied successfully!"
                discount_amount = round(0.30 * session.get('subtotal', 0.00), 2)  # Apply 30% discount
                session['discount_amount'] = discount_amount
            else:
                discount_valid = False
                discount_message = "Invalid discount code."
                session['discount_amount'] = 0.00  # Reset any previous discount

    # Delivery cost
    delivery_cost = session.get('delivery_cost', 0.00)

    # Fetch cart items from session
    cart_ids = session.get('cart', [])
    cart_items = [
        {
            'id': product.product_id,
            'name': product.name,
            'price': product.price,
            'image_url': product.image_url,
            'quantity': cart_ids.count(product_id)
        }
        for product_id in set(cart_ids)
        if (product := product_service.get_product_details(product_id))
    ]

    # Calculate totals
    subtotal = sum(item['price'] * item['quantity'] for item in cart_items)
    tax = round(subtotal * 0.1, 2)  # 10% tax
    discount_amount = session.get('discount_amount', 0.00)
    new_subtotal = subtotal - discount_amount
    total = round(new_subtotal + tax + delivery_cost, 2)

    # Save totals to session
    session['subtotal'] = subtotal
    session['tax'] = tax
    session['total'] = total

    return render_template(
        'cart.html',
        cart_items=cart_items,
        discount_message=discount_message,
        discount_valid=discount_valid,
        discount_applied=discount_amount > 0,
        discount_amount=discount_amount,
        new_subtotal=new_subtotal,
        tax=tax,
        delivery_cost=delivery_cost,
        total=total
    )
# Route to handle checkout
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        # Redirect to confirmation page after payment details are entered
        return redirect(url_for('confirmation'))
    return render_template('checkout.html')


@app.route('/confirmation', methods=['GET', 'POST'])
def confirmation():
    # Retrieve cart and order details from session
    ordered_items = [
        {
            'name': product_service.get_product_details(item_id).name,
            'image_url': product_service.get_product_details(item_id).image_url,
            'price': product_service.get_product_details(item_id).price,
            'quantity': session['cart'].count(item_id),
        }
        for item_id in set(session.get('cart', []))
    ]

    first_name = session.get('user_firstname', 'John')
    last_name = session.get('user_lastname', 'Doe')
    order_number = 123456  # Example static order number
    subtotal = session.get('subtotal', 0.00)
    tax = session.get('tax', 0.00)
    discount = session.get('discount_amount', 0.00)
    delivery = session.get('delivery_cost', 0.00)
    total = session.get('total', 0.00)

    return render_template(
        'confirmation.html',
        ordered_items=ordered_items,
        first_name=first_name,
        last_name=last_name,
        order_number=order_number,
        subtotal=subtotal,
        tax=tax,
        discount=discount,
        delivery=delivery,
        total=total
    )

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        session['cart'] = cart
        flash(f'Product {product_id} "removed from cart.' f'Your cart has been removed successfully!')
    return redirect(url_for('cart'))

@app.route('/update_cart/<int:product_id>', methods=['POST'])
def update_cart(product_id):
    action = request.form.get('action')
    cart = session.get('cart', [])

    if action == 'increase':
        # Add the product ID to the cart list for quantity increase
        cart.append(product_id)
    elif action == 'decrease':
        # Remove one instance of the product ID from the cart list
        if product_id in cart:
            cart.remove(product_id)

    # Update the cart in the session
    session['cart'] = cart

    flash("Cart updated successfully!", "success")
    return redirect(url_for('cart'))

# _____________________________ WISHLIST ROUTES _____________________________ #

@app.route('/add_to_wishlist/<int:product_id>')
@login_required
def add_to_wishlist(product_id):
    wishlist = session.setdefault('wishlist', [])
    if product_id not in wishlist:
        wishlist.append(product_id)
        session['wishlist'] = wishlist
        flash(f'Product {product_id} added to wishlist!', 'success')
    else:
        flash('Product already in wishlist.', 'info')
    return redirect(url_for('show_products'))

@app.route('/wishlist')
def view_wishlist():
    wishlist_ids = session.get('wishlist', [])
    wishlist_items = [product_service.get_product_details(product_id) for product_id in wishlist_ids]
    return render_template('wishlist.html', wishlist_items=wishlist_items)

@app.route('/remove_from_wishlist/<int:product_id>')
def remove_from_wishlist(product_id):
    wishlist = session.get('wishlist', [])
    if product_id in wishlist:
        wishlist.remove(product_id)
        session['wishlist'] = wishlist
        flash(f'Product {product_id} removed from wishlist.')
    return redirect(url_for('view_wishlist'))

# _____________________________ STATIC PAGES _____________________________ #

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/upcoming_releases')
def upcoming_releases():
    return render_template('upcoming_releases.html')

# _____________________________ MAIN ENTRY _____________________________ #

if __name__ == '__main__':
    app.run(debug=True)