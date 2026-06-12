

class CartPage:
    def __init__(self, page):
        self.page = page

    def verify_product(self):
        return self.page.locator(".inventory_item_name").text_content()