from playwright.sync_api import Page

class RegistrationPage:
    def __init__(self, page: Page):
        self.page = page

        self.txt_firstname = page.locator('#input-firstname')
        self.txt_lastname = page.locator('#input-lastname')
        self.txt_email = page.locator('#input-email')
        self.txt_telephone = page.locator('#input-telephone')
        self.txt_password = page.locator('#input-password')
        self.txt_confirm_password = page.locator('#input-confirm')

        self.chk_policy = page.locator('input[name="agree"]')
        self.btn_continue = page.locator('input[value="Continue"]')

        self.msg_confirmation = page.locator('h1:has-text("Your Account Has Been Created!")')

    def set_first_name(self, fname: str):
        self.txt_firstname.fill(fname)

    def set_last_name(self, lname: str):
        self.txt_lastname.fill(lname)

    def set_email(self, email: str):
        self.txt_email.fill(email)

    def set_telephone(self, tel: str):
        self.txt_telephone.fill(tel)

    def set_password(self, pwd: str):
        self.txt_password.fill(pwd)

    def set_confirm_password(self, pwd: str):
        self.txt_confirm_password.fill(pwd)

    def set_privacy_policy(self):
        self.chk_policy.check()

    def click_continue(self):
        self.btn_continue.click()

    def get_confirmation_msg(self):
        return self.msg_confirmation

    def complete_registration(self, user_data: dict):

        self.set_first_name(user_data["firstName"])
        self.set_last_name(user_data["lastName"])
        self.set_email(user_data["email"])
        self.set_telephone(user_data["telephone"])
        self.set_password(user_data["password"])
        self.set_confirm_password(user_data["password"])
        self.set_privacy_policy()
        self.click_continue()

        # Return confirmation message element for validation
        return self.msg_confirmation
