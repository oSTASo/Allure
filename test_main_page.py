import pytest
import allure
from pages.basket_page import BasketPage
from pages.main_page import MainPage
from pages.login_page import LoginPage


@allure.epic('Test login from main page')
@pytest.mark.login_guest
class TestLoginFromMainPage:

    @allure.feature('Test guest can go to login page')
    def test_guest_can_go_to_login_page(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.should_be_login_link()

    @allure.feature('Test guest should see login link')
    def test_guest_should_see_login_link(self, browser):
        link = 'http://selenium1py.pythonanywhere.com/'
        page = MainPage(browser, link)
        page.open()
        page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/'
    page = BasketPage(browser, link)
    page.open()
    page.click_show_basket()
    page.check_empty_basket()
    page.take_screenshot()
    page.check_message_empty_basket(), 'The basket is not empty'

