

class Homepage:
    def __init__(self, page):
        self.page = page

    def add_to_cart(self):
        self.page.click("#add-to-cart-sauce-labs-backpack")
    
    def open_cart(self):
        self.page.click(".shopping_cart_link")