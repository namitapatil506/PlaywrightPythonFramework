from playwright.sync_api import Page

class LogoutPage:
    def __init__(self, page:Page):
        self.page=page
        self.btn_continue = page.locator('.btn.btn-primary')

    def click_continue(self):
        try:
            self.btn_continue.click()
        except Exception as e:
            print(f" Exception while clicking 'Continue' button: {e}")
            raise

    def get_continue_button(self):
        try:
            return self.btn_continue
        except Exception as e:
            print(f" Exception while fetching 'Continue' button locator: {e}")
            return None
