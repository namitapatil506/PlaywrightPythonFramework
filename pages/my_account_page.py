from playwright.sync_api import Page
from pages.logout_page import LogoutPage


class MyAccountPage:
    def __init__(self, page: Page):
        self.page = page

        self.msg_heading = page.locator('h2:has-text("My Account")')
        self.lnk_logout = page.locator("text='Logout'").nth(1)

    def get_my_account_page_heading(self):
        try:
            return self.msg_heading
        except Exception as e:
            print(f"Error returning My Account page heading: {e}")
            return None

    def click_logout(self) -> LogoutPage:
        try:
            self.lnk_logout.click()
            return LogoutPage(self.page)
        except Exception as e:
            print(f"Unable to click Logout link: {e}")
            raise

    def get_page_title(self) -> str:
        try:
            return self.page.title()
        except Exception as e:
            print(f"Error retrieving page title: {e}")
            return ""
