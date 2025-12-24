from playwright.sync_api import Page, expect
from pages.checkout_page import CheckoutPage  # Adjust import path as per your project structure


class ShoppingCartPage:
    def __init__(self, page: Page):
        self.page = page
        self.lbl_total_price = page.locator(
            "//*[@id='content']/div[2]/div/table//strong[text()='Total:']//following::td")
        self.btn_checkout = page.locator("a.btn.btn-primary")

    def get_total_price(self):
        try:
            return self.lbl_total_price
        except Exception as e:
            print(f"Unable to retrieve total price: {e}")
            return None

    def click_on_checkout(self) -> CheckoutPage:
        try:
            self.btn_checkout.click()
            return CheckoutPage(self.page)
        except Exception as e:
            print(f"Error clicking on checkout button: {e}")
            raise e  # Re-raise to fail the test if critical navigation fails

    def is_page_loaded(self) :
        try:
            return self.btn_checkout
        except Exception as e:
            print(f"Error verifying shopping cart page load: {e}")
            return None
