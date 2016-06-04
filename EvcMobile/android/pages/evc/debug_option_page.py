#coding:utf-8
import time

from page_objects import PageElement
from selenium.webdriver.common.by import By
from android.pages.evc.abstract_base_evc_android_page import AbstractBaseEvcAndroidPage
from android.pages.evc.class_room_entry_page import ClassRoomEntryPage
from android.pages.evc.evc_room_page import EvcRoomPage


class DebugOptionPage(AbstractBaseEvcAndroidPage):
    WAIT_PAGE_LOAD_TIME_OUT = 5

    LOAD_CLASS_ROOM_IN_WEBVIEW_XPATH = "//*[@text='Load Classroom in WebView']"
    START_SIMPLE_CLASS_DEMO_XPATH = "//*[@resource-id='com.ef.evc2015:id/simpleClassButton']"
    LOAD_JOCKEY_JS_DEMO = "//*[@resource-id='com.ef.evc2015:id/jockeyJs']"
    LOAD_LOGIN_PAGE_IN_WEBVIEW = "//*[@resource-id='com.ef.evc2015:id/loginPage']"

    load_class_room_in_webview_link = PageElement(xpath=LOAD_CLASS_ROOM_IN_WEBVIEW_XPATH)
    start_simple_class_in_webview = PageElement(xpath=START_SIMPLE_CLASS_DEMO_XPATH)
    load_jockey_js_demo = PageElement(xpath=LOAD_JOCKEY_JS_DEMO)
    load_login_page_in_webview = PageElement(xpath=LOAD_LOGIN_PAGE_IN_WEBVIEW)

    def __init__(self, driver):
		AbstractBaseEvcAndroidPage.__init__(self, driver)

    def is_target_page(self):
        return self.is_element_displayed_on_page(self.load_class_room_in_webview_link)

    def go_to_class_room_entry_page(self):
        if self.is_element_displayed_on_page(self.load_class_room_in_webview_link):
            self.load_class_room_in_webview_link.click()
        return ClassRoomEntryPage(self.driver)

if __name__ == '__main__':
	pass
