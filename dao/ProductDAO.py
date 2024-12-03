# ProductDAO.py
from model.Product import Product



class ProductDAO:
    def __init__(self):
        # Initialize with some dummy products
        self.products = [
            Product(1, "Nike Air Mag",
                    "Back to the Future (2016)",
                    "Sneakers", "10UK", "Silver Metallic", "Nike", 61000.00, "/static/images/AirMag.jpeg"),

            Product(2, "Adidas YEEZY 350 v2 'Dazzling Blue' Sneakers", "Round toe, front lace-up fastening, YEEZY Primeknit upper, branded insole, signature cushioned Boost midsole, rubber sole, designed by Kanye West", "Sneakers", "7UK - 12UK", "Black", "Adidas YEEZY", 500.00, "/static/images/YEEZY.jpeg"),

            Product(3, "Nike x Sean Wotherspoon Air Max 1/97", "Supplied by a premier sneaker marketplace dealing with unworn, already sold out, in-demand rarities. Each product is rigorously inspected by experienced experts guaranteeing authenticity. Created by popular demand. Sean Wotherspoon’s winning Air Max sneaker design from the RevolutionAIR voting campaign in early 2017 is now a reality. His creation, the Air Max 1/97 VF SW, features a hybrid design of the Air Max 97 upper in a unique multi-colored corduroy build on top of the iconic tooling of the Air Max 1. Released early in November 2017, Sean actually drove around Los Angeles giving out free pairs of the coveted Air Max 1/97 before the official retail release on Air Max Day 2018.", "Sneakers", "8UK - 11UK", "Yellow", "Nike", 2100.00, "/static/images/SW.jpeg"),

            Product(4, "Jordan x Travis Scott Air Jordan 1 Low OG 'Reverse Mocha'", "The Air Jordan 1 colourway Reverse Mocha designed by Travis Scott and Jordan Brand has finally arrived. This sneaker is crafted from a mix of suede and leather panels in neutral tones - Sail and Ridgerock - while some University red accents appear on the tongue label and embroidered logo on the heel. The Cactus Jack's signature reverse Swoosh logo makes the design stand out while a rubber outsole completes it with comfort.", "Sneakers", "8UK - 11UK", "Mocha", "Jordan x Travis Scott", 1200.00, "/static/images/travis.jpeg"),

            Product(5, "SALOMON XT-6 EXPANSE","A valued member of the XT-6 lineage, XT-6 Expanse sneaker brings new texture to the family of trail legends. Heritage-inspired materials are layered over stitched panels and a Sensifit construction - giving a more layered, retro feel. The EXPANSE is just as ready as its predecessors for the urban landscape.","Sneakers", "8UK - 11UK", "White, Metal and Black", "Salomon", 175.00, "/static/images/Salomon.jpeg"),

            Product(6, "GUCCI SCREENER SNEAKER","Designed for the city streets, these Gucci Screener Sneakers are crafted with a leather upper, whilst perforated fabric trims offer both breathability and contrast detailing. On the side, a classic web stripe completes the design.","Sneakers", "5UK - 11UK", "White, Green and Red", "Gucci", 890.00, "/static/images/Gucci.jpeg"),

            Product(7, "AMIRI BANDANA DENIM SKEL TOP LOW SNEAKER","Hand cut and sewn on these AMIRI Bandana Denim Skel Top Low Sneakers, the label’s unique bone motif defines the piece. Crafted with a leather upper, the striking skelton detailing appears in contrasting denim. With overlays and a perforated toe box, a bandana print is all kinds of classic.","Sneakers", "6UK - 13UK", "Black and White", "Amiri", 680.00, "/static/images/Amiri.jpeg"),

            Product(8, "NEW BALANCE M1906REE","Whether you’re hitting your personal best or keeping your look low-key, these 1906 Sneakers from New Balance have got you covered. Optimised for continuous comfort, they’re structured using an ABZORB midsole and N-ergy cushioning - while stability web outsole technology provides plenty of arch support. Decorated with hits of silver throughout the mesh uppers and rubber outsole, this dynamic design promises to be the most reliable in any rotation.","Sneakers", "4UK - 12UK", "Silver Metallic", "New Balance", 165.00, "/static/images/NewBalance1.jpeg"),

        ]

    def get_all_products(self):
        return self.products

    def get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
