#coding:utf-8

from page_objects import PageElement
from selenium.webdriver.common.by import By

from ios.pages.evc.abstract_base_evc_ios_page import AbstractBaseEvcIosPage


class LoginPage(AbstractBaseEvcIosPage):
    EMAIL_OR_USERNAME_TEXT_FIELD_XPATH = "//UIAWebView/UIATextField[@value='电子邮件或者用户名']"
    PASSWORD_TEXT_FIELD_XPATH = "//UIAWebView/UIASecureTextField[@value='密码']"
    LOGIN_BUTTON_XPATH = "//UIAWebView/UIAButton[@name='登录']"


    email_or_username_text_field = PageElement(xpath=EMAIL_OR_USERNAME_TEXT_FIELD_XPATH)
    password_text_field = PageElement(xpath=PASSWORD_TEXT_FIELD_XPATH)
    login_button = PageElement(xpath=LOGIN_BUTTON_XPATH)

    def __init__(self, driver):
		AbstractBaseEvcIosPage.__init__(self, driver);

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

if __name__ == '__main__':
    pass
