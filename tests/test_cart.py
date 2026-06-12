

from pages.login_page import LoginPage
from pages.home_page import Homepage
from pages.cart_page import CartPage

def test_add_cart(page):
    page.goto("https://www.saucedemo.com/")
    
    # Login
    login_page = LoginPage(page)
    login_page.login(
        "standard_user",
        "secret_sauce"
    )
    Homepage(page).add_to_cart()
    Homepage(page).open_cart()
    
    product_name = CartPage(page).verify_product()
    assert product_name == "Sauce Labs Backpack"