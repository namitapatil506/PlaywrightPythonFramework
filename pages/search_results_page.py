from playwright.sync_api import Page
from pages.product_page import ProductPage


class SearchResultsPage:

    def __init__(self, page: Page):
        self.page = page

        self.search_page_header = page.locator("#content h1", has_text="Search -")
        self.search_products = page.locator("h4 > a")

    def get_search_results_page_header(self):
        try:
            return self.search_page_header
        except Exception as e:
            print(f"Error fetching search results page header: {e}")
            return None

    def is_product_exist(self, product_name: str):
        try:
            count = self.search_products.count()
            for i in range(count):
                product = self.search_products.nth(i)
                title = product.text_content()
                if title and title.strip() == product_name:
                    return product
        except Exception as e:
            print(f"Error while checking product existence: {e}")
        return None

    def select_product(self, product_name: str) -> ProductPage | None:
        try:
            count = self.search_products.count()
            for i in range(count):
                product = self.search_products.nth(i)
                title = product.text_content()
                if title and title.strip() == product_name:
                    product.click()
                    return ProductPage(self.page)
            print(f"Product not found: {product_name}")
        except Exception as e:
            print(f"Error while selecting product: {e}")
        return None

    def get_product_count(self):
        try:
            return self.search_products
        except Exception as e:
            print(f"Error while getting product count: {e}")
            return None
