# ProductService.py
from dao.ProductDAO import ProductDAO


class ProductService:
    def __init__(self):
        self.product_dao = ProductDAO()

    def get_all_products(self):
        return self.product_dao.get_all_products()

    def get_product_details(self, product_id):
        return self.product_dao.get_product_by_id(product_id)
