class Product:
    def __init__(self, product_id, name, description, type_, size, color, brand, price, image_url):
        self.product_id = product_id
        self.name = name
        self.description = description
        self.type = type_
        self.size = size
        self.color = color
        self.brand = brand
        self.price = price
        self.image_url = image_url

    def __repr__(self):
        return f"<Product(product_id={self.product_id}, name={self.name})>"

