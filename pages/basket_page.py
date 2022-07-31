from .locators import ProductPageLocators
from .product_page import ProductPage


class BasketPage(ProductPage):

    def check_empty_basket(self):
        assert not self.is_element_present(*ProductPageLocators.CURRENT_NAME)

    def check_message_empty_basket(self):
        need_text = 'Your basket is empty.'
        assert need_text in self.browser.find_element(*ProductPageLocators.BASKET_EMPTY).text
