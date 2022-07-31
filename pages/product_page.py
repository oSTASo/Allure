from .locators import ProductPageLocators
from .base_page import BasePage


class ProductPage(BasePage):

    def click_btn_add_basket(self):
        self.browser.find_element(*ProductPageLocators.BTN_ADD_BASKET).click()

    def check_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        assert self.browser.find_element(*ProductPageLocators.CURRENT_NAME).text == \
               product_name, 'product name is wrong'

    def check_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert self.browser.find_element(*ProductPageLocators.CURRENT_PRICE).text == \
               product_price, 'product price is wrong'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_dissapear_of_success_message(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"
