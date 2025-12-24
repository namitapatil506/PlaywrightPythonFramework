from playwright.sync_api import Page, expect
from pages.shopping_cart_page import ShoppingCartPage


class ProductPage:
    def __init__(self, page: Page):
        self.page = page

        self.txt_quantity = page.locator('input[name="quantity"]')
        self.btn_add_to_cart = page.locator('#button-cart')
        self.cnf_msg = page.locator('.alert.alert-success.alert-dismissible')
        self.btn_items = page.locator('#cart')
        self.lnk_view_cart = page.locator('strong:has-text("View Cart")')

    def set_quantity(self, qty: str):
        try:
            self.txt_quantity.fill('')   # Clear existing value
            self.txt_quantity.fill(qty)  # Enter new quantity
        except Exception as e:
            print(f"Error while setting quantity: {e}")
            raise

    def add_to_cart(self):
        try:
            self.btn_add_to_cart.click()
        except Exception as e:
            print(f"Error while clicking 'Add to Cart': {e}")
            raise

    def get_confirmation_message(self):
        try:
            return self.cnf_msg
        except Exception as e:
            print(f"Confirmation message not found: {e}")
            return None

    def click_items_to_navigate_to_cart(self):
        try:
            self.btn_items.click()
        except Exception as e:
            print(f"Error while clicking cart items button: {e}")
            raise

    def click_view_cart(self) -> ShoppingCartPage:
        try:
            self.lnk_view_cart.click()
            return ShoppingCartPage(self.page)
        except Exception as e:
            print(f"Error while clicking 'View Cart': {e}")
            raise

    def add_product_to_cart(self, quantity: str):
        """
        Combined workflow to:
        1. Set product quantity
        2. Add product to the cart
        3. Validate confirmation message (optional)
        """
        try:
            self.set_quantity(quantity)
            self.add_to_cart()
            expect(self.get_confirmation_message()).to_be_visible()
        except Exception as e:
            print(f"Error in add_product_to_cart workflow: {e}")
            raise
