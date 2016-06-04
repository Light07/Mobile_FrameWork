#coding:utf-8

from page_objects import PageElement
from selenium.webdriver.common.by import By
from android.pages.evc.abstract_base_evc_android_page import AbstractBaseEvcAndroidPage
from android.pages.evc.debug_option_page import DebugOptionPage
from android.pages.evc.mybookings_page import MyBookingPage

class LoginPage(AbstractBaseEvcAndroidPage):
    EMAIL_OR_USERNAME_TEXT_FIELD_XPATH ="//*[@resource-id='username']"
    PASSWORD_TEXT_FIELD_XPATH = "//*[@resource-id='password']"
    LOGIN_BUTTON_XPATH = "//*[@content-desc='登录']"
    LOGIN_ERROR_XPATH = "//*[@content-desc='未注册的用户名或者密码错误']"
    BOOKING_BUTTON_XPATH = "//evc.widget.Button"
    DEBUG_BUTTON_PATH = "//*[@text='DEBUG']"

    email_or_username_text_field = PageElement(xpath=EMAIL_OR_USERNAME_TEXT_FIELD_XPATH)
    password_text_field = PageElement(xpath=PASSWORD_TEXT_FIELD_XPATH)
    login_button = PageElement(xpath=LOGIN_BUTTON_XPATH)
    error_message = PageElement(xpath=LOGIN_ERROR_XPATH)
    debug_button = PageElement(xpath=DEBUG_BUTTON_PATH)

    def __init__(self, driver):
		AbstractBaseEvcAndroidPage.__init__(self, driver);

    def is_target_page(self):
        return self.is_element_displayed(By.XPATH, self.EMAIL_OR_USERNAME_TEXT_FIELD_XPATH)

    def set_username_or_email(self, username):
        self.email_or_username_text_field.click()
        self.email_or_username_text_field.send_keys(username)

    def set_password(self, password):
        self.password_text_field.click()
        self.password_text_field.send_keys(password)

    def click_login_button(self):
        self.login_button.click()

    def login(self, username, password):
        self.set_username_or_email(username)
        self.set_password(password)
        self.click_login_button()
        return MyBookingPage(self.driver)

    def go_to_debug_option_page(self):
        self.debug_button.click()
        return DebugOptionPage(self.driver)

if __name__ == '__main__':
	pass
