import time

from page_objects import PageElement
from selenium.webdriver.common.keys import Keys

from ios.pages.evc.abstract_base_evc_ios_page import AbstractBaseEvcIosPage


class ClassroomPage(AbstractBaseEvcIosPage):

    CHAT_ICON_XPATH = "//span[contains(@class,  'icon-chat')]"
    CLASS_NOTES_ICON_XPATH = "//UIAWebView/UIAStaticText[8]"
    ATTENDEES_ICON_XPATH = "//UIAWebView/UIAStaticText[9]"
    CLASS_ROOM_INFO_ICON_XPATH = "//UIAWebView/UIAStaticText[10]"
    PPT_ICON_XPATH = "//UIAWebView/UIAStaticText[11]"
    RAISE_HAND_ICON_XPATH = "//UIAWebView/UIAStaticText[12]"
    MIC_ICON_XPATH = "//UIAWebView/UIAStaticText[13]"
    CAMERA_ICON_XPATH = "//UIAWebView/UIAStaticText[14]"
    SEND_MESSAGE_TEXT_FIELD_XPATH = "//UIAWebView/UIATextField"

    WAIT_FOR_SIDE_MENU_EXPAND_TIME = 1

    chat_icon = PageElement(xpath=CHAT_ICON_XPATH)
    send_message_text_field = PageElement(xpath=SEND_MESSAGE_TEXT_FIELD_XPATH)

    def is_target_page(self):
        return self.is_element_exist('//UIAWebView/UIAImage')

    def expand_side_menu(self):
        web_view = self.driver.find_element_by_xpath('//UIAWebView')
        web_view.click()
        time.sleep(self.WAIT_FOR_SIDE_MENU_EXPAND_TIME)

    def click_chat_icon(self):
        contexts = self.driver.contexts
        webviews = []
        for context in contexts:
            if 'WEBVIEW' in context:
                webviews.append(context)

        self.driver.switch_to.context(webviews[1])
        # Must click twice, or it takes no effect
        self.chat_icon.click()
        self.chat_icon.click()

        time.sleep(5)

        self.driver.switch_to.context('NATIVE_APP')

    def set_send_message(self, message):
        self.send_message_text_field.click()
        self.send_message_text_field.send_keys(message)

    def send_chat_message(self):
        self.send_message_text_field.send_keys(Keys.ENTER)
        self.send_message_text_field.send_keys(Keys.ENTER)