# ProductDAO.py
from model.Product import Product


class ProductDAO:
    def __init__(self):
        # Initialize with some dummy products
        self.products = [
            Product(1, "Jordan x Travis Scott Air Jordan 1 Low OG 'Reverse Mocha'", "The Air Jordan 1 colourway Reverse Mocha designed by Travis Scott and Jordan Brand has finally arrived. This sneaker is crafted from a mix of suede and leather panels in neutral tones - Sail and Ridgerock - while some University red accents appear on the tongue label and embroidered logo on the heel. The Cactus Jack's signature reverse Swoosh logo makes the design stand out while a rubber outsole completes it with comfort.", "Sneakers", "8UK - 11UK", "Mocha", "Jordan x Travis Scott", 1200.00, "/static/images/travis.jpeg"),

            Product(2, "Adidas YEEZY 350 v2 'Dazzling Blue' Sneakers", "Round toe, front lace-up fastening, YEEZY Primeknit upper, branded insole, signature cushioned Boost midsole, rubber sole, designed by Kanye West", "Sneakers", "7UK - 12UK", "Black", "Adidas YEEZY", 500.00, "/static/images/YEEZY.jpeg"),

            Product(3, "Nike x Sean Wotherspoon Air Max 1/97", "Supplied by a premier sneaker marketplace dealing with unworn, already sold out, in-demand rarities. Each product is rigorously inspected by experienced experts guaranteeing authenticity. Created by popular demand. Sean Wotherspoon’s winning Air Max sneaker design from the RevolutionAIR voting campaign in early 2017 is now a reality. His creation, the Air Max 1/97 VF SW, features a hybrid design of the Air Max 97 upper in a unique multi-colored corduroy build on top of the iconic tooling of the Air Max 1. Released early in November 2017, Sean actually drove around Los Angeles giving out free pairs of the coveted Air Max 1/97 before the official retail release on Air Max Day 2018.", "Sneakers", "8UK - 11UK", "Yellow", "Nike", 2100.00, "/static/images/SW.jpeg")
        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
