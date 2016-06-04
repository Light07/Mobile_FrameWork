#coding:utf-8
import time

from page_objects import PageElement
from selenium.webdriver.common.by import By
from android.pages.evc.abstract_base_evc_android_page import AbstractBaseEvcAndroidPage
from android.pages.evc.evc_room_page import EvcRoomPage

class ClassRoomEntryPage(AbstractBaseEvcAndroidPage):
    WAIT_PAGE_LOAD_TIME_OUT = 5

    YOUR_NAME_XPATH = "//*[@content-desc='YOUR NAME ']/*[@class='android.view.View'][2]/*[@class='android.widget.EditText']"
    ROOM_NAME_XPATH = "//*[@content-desc='ROOM NAME ']/*[@class='android.view.View'][2]/*[@class='android.widget.EditText']"
    SPINNER__XPATH = "//*[@class='android.widget.Spinner']"
    CONTENT_ID_DROP_DOWN_XATH = "//*[@class='android.widget.ListView']"
    JOIN_BUTTON_XPATH = "//*[@class='android.widget.Button' and contains(@content-desc, 'JOIN')]"
    ROOM_DURATION_XPATH = "//*[@content-desc='CONTENT ID DURATION (MINS) ']/*[@class='android.view.View'][4]/*[@class='android.widget.EditText']"

    your_name_input_field = PageElement(xpath=YOUR_NAME_XPATH)
    room_name_input_field = PageElement(xpath=ROOM_NAME_XPATH)
    spinner = PageElement(xpath=SPINNER__XPATH)
    content_id_drop_down = PageElement(xpath=CONTENT_ID_DROP_DOWN_XATH)
    duration_input_field = PageElement(xpath=ROOM_DURATION_XPATH)
    join_button = PageElement(xpath=JOIN_BUTTON_XPATH)

    def __init__(self, driver):
		AbstractBaseEvcAndroidPage.__init__(self, driver)

    def is_target_page(self):
        return self.is_element_displayed(By.XPATH, self.SPINNER__XPATH)

    def get_class_room_name(self):
        return self.room_name_input_field.get_attribute("name")

    def get_class_room_duration(self):
        return self.duration_input_field.get_attribute("name")

    def go_to_evc_room(self, user_name, room_name):
        hint_user_name_len =len(self.your_name_input_field.get_attribute("name"))
        for i in range(hint_user_name_len):
            self.your_name_input_field.click()
            self.driver.press_keycode(67)

        self.your_name_input_field.set_text(user_name)
        hint_room_name_len = len(self.room_name_input_field.get_attribute("name"))
        for i in range(hint_room_name_len):
            self.room_name_input_field.click()
            self.driver.press_keycode(67)
        self.room_name_input_field.set_text(room_name)
        self.join_button.click()
        return EvcRoomPage(self.driver)

if __name__ == '__main__':
	pass
