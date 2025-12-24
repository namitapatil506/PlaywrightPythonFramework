from playwright.sync_api import Page


class CheckoutPage:
    def __init__(self, page: Page):
        self.page = page

        self.radio_guest = page.locator('input[value="guest"]')
        self.btn_continue = page.locator('#button-account')
        self.txt_first_name = page.locator('#input-payment-firstname')
        self.txt_last_name = page.locator('#input-payment-lastname')
        self.txt_address1 = page.locator('#input-payment-address-1')
        self.txt_address2 = page.locator('#input-payment-address-2')
        self.txt_city = page.locator('#input-payment-city')
        self.txt_pin = page.locator('#input-payment-postcode')
        self.drp_country = page.locator('#input-payment-country')
        self.drp_state = page.locator('#input-payment-zone')
        self.btn_continue_billing_address = page.locator('#button-payment-address')
        self.btn_continue_delivery_address = page.locator('#button-shipping-address')
        self.txt_delivery_method = page.locator('textarea[name="comment"]')
        self.btn_continue_shipping_address = page.locator('#button-shipping-method')
        self.chkbox_terms = page.locator('input[name="agree"]')
        self.btn_continue_payment_method = page.locator('#button-payment-method')
        self.lbl_total_price = page.locator('strong:has-text("Total:") + td')
        self.btn_conf_order = page.locator('#button-confirm')
        self.lbl_order_con_msg = page.locator('#content h1')

    def get_checkout_page_title(self) -> str:
        try:
            return self.page.title()
        except Exception as e:
            print(f" Exception while getting Checkout page title: {e}")
            return None

    def choose_checkout_option(self, checkout_option: str):
        try:
            if checkout_option.lower() == "guest checkout":
                self.radio_guest.click()
        except Exception as e:
            print(f" Exception while choosing checkout option '{checkout_option}': {e}")
            raise

    def click_continue(self):
        try:
            self.btn_continue.click()
        except Exception as e:
            print(f" Exception while clicking Continue: {e}")
            raise

    def set_first_name(self, first_name: str):
        self.txt_first_name.fill(first_name)

    def set_last_name(self, last_name: str):
        self.txt_last_name.fill(last_name)

    def set_address1(self, address1: str):
        self.txt_address1.fill(address1)

    def set_address2(self, address2: str):
        self.txt_address2.fill(address2)

    def set_city(self, city: str):
        self.txt_city.fill(city)

    def set_pin(self, pin: str):
        self.txt_pin.fill(pin)

    def set_country(self, country: str):
        self.drp_country.select_option(label=country)

    def set_state(self, state: str):
        self.drp_state.select_option(label=state)

    def click_continue_after_billing_address(self):
        self.btn_continue_billing_address.click()

    def click_continue_after_delivery_address(self):
        self.btn_continue_delivery_address.click()

    def set_delivery_method_comment(self, message: str):
        self.txt_delivery_method.fill(message)

    def click_continue_after_delivery_method(self):
        self.btn_continue_shipping_address.click()

    def select_terms_and_conditions(self):
        self.chkbox_terms.check()

    def click_continue_after_payment_method(self):
        self.btn_continue_payment_method.click()

    def get_total_price_before_confirm(self):
        return self.lbl_total_price

    def click_confirm_order(self):
        try:
            self.btn_conf_order.click()
        except Exception as e:
            print(f" Exception while confirming order: {e}")
            raise

    def is_order_placed(self):
        try:
            # Handle alert/dialog popups automatically if they appear
            self.page.on("dialog", lambda dialog: dialog.accept())
            return self.lbl_order_con_msg
        except Exception as e:
            print(f" Exception while checking order confirmation: {e}")
            return None
