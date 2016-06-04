#coding:utf-8
import time

from page_objects import PageElement
from selenium.webdriver.common.by import By
from android.pages.evc.abstract_base_evc_android_page import AbstractBaseEvcAndroidPage

class EvcRoomPage(AbstractBaseEvcAndroidPage):
    WAIT_PAGE_LOAD_TIME_OUT = 5

    SCREEN_XPATH = "//android.webkit.WebView[@index=0 and @content-desc='EVC15']"
    CHAT_XPATH = "//android.webkit.WebView[@index=0 and @content-desc='EVC15']/android.view.View[@index=1]"
    CLASS_NOTE_XPATH = "//android.view.View[@index=2]"
    ATTENDEES_XPATH = "//android.view.View[@index=3]"
    WEBVIEW_XPATH = "//android.webkit.WebView[@resource-id='com.ef.evc2015:id/webView']"
    SEND_MESSAGE_XPATH ="//*[contains(@content-desc, 'Send Message...')]"
    PPT_AREA_PATH = "//android.view.View[@index=0]"

    web_view_pic =  PageElement(xpath=WEBVIEW_XPATH)
    screen_panel = PageElement(xpath=SCREEN_XPATH)
    chat_button = PageElement(xpath=CHAT_XPATH)
    send_message_input_box = PageElement(xpath=SEND_MESSAGE_XPATH)
    ppt_area = PageElement(xpath=PPT_AREA_PATH)

    def __init__(self, driver):
		AbstractBaseEvcAndroidPage.__init__(self, driver)

    def is_target_page(self):
        return self.is_element_displayed(By.XPATH, self.WEBVIEW_XPATH)

    def select_chat_button(self):
        time.sleep(self.WAIT_PAGE_LOAD_TIME_OUT)
        self.ppt_area.click()
        self.driver.switch_to.context("NATIVE_APP")
        if self.is_element_displayed_on_page(self.chat_button):
            self.chat_button.click()

    def send_text_through_chat_dialog(self, message_code):
        if self.is_element_displayed_on_page(self.send_message_input_box):
            self.send_message_input_box.click()
            self.driver.switch_to.context("NATIVE_APP")
            self.send_message_input_box.click()
            self.driver.press_keycode(message_code)
            self.driver.press_keycode(66)
if __name__ == '__main__':
	pass
