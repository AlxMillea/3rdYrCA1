from urllib import request
from flask import Flask, render_template, request, redirect, url_for, session, flash
from service.ProductService import ProductService
from service.UserService import UserService

app = Flask(__name__)
app.secret_key = "your_secret_key"
product_service = ProductService()
user_service = UserService()


@app.route('/')
def home():
    products = product_service.get_all_products()
    return render_template('index.html', products=products)


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


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = user_service.authenticate_user(email, password)
        if user:
            session['user_id'] = user.userid
            session['user_role'] = user.role
            session['user_firstname'] = user.firstname
            if user.role == 'admin':
                return redirect(url_for('admin_dashboard'))
            else:
                return redirect(url_for('home'))
        else:
            flash("Invalid credentials. Please try again.", "danger")
            return redirect(url_for('login'))
    return render_template('login.html')


# Admin dashboard route
@app.route('/admin')
def admin_dashboard():
    if 'user_role' in session and session['user_role'] == 'admin':
        flash("You are an admin. Welcome back!", "success")
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


@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(product_id)
    flash(f'Product {product_id} added to cart!')
    return redirect(url_for('show_products'))


@app.route('/cart')
def view_cart():
    cart = session.get('cart', [])
    cart_items = [product_service.get_product_details(product_id) for product_id in cart]

    # Calculate the subtotal
    subtotal = sum(item.price for item in cart_items if item)

    return render_template('cart.html', cart_items=cart_items, subtotal=subtotal)


@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', [])
    if product_id in cart:
        cart.remove(product_id)
        session['cart'] = cart
        flash(f'Product {product_id} removed from cart.')
    return redirect(url_for('view_cart'))


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/admin/view_reports')
def view_reports():
    if 'user_role' in session and session['user_role'] == 'admin':
        # Dummy content for reports, can be expanded to real reporting data
        return render_template('view_reports.html')
    else:
        flash("You do not have permission to access this page.")
        return redirect(url_for('login'))


@app.route('/upcoming_releases')
def upcoming_releases():
    return render_template('upcoming_releases.html')


if __name__ == '__main__':
    app.run(debug=True)
