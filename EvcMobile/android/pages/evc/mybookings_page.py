#coding:utf-8

from page_objects import PageElement
from selenium.webdriver.common.by import By

from android.pages.evc.abstract_base_evc_android_page import AbstractBaseEvcAndroidPage
from android.pages.evc.evc_room_page import EvcRoomPage


class MyBookingPage(AbstractBaseEvcAndroidPage):

    BOOKING_BUTTON_XPATH = "//*[@class='android.widget.Button']"
    ENTER_CLASS_BUTTON_XPATH ="//*[@content-desc='进入教室 ']"

    book_button = PageElement(xpath=BOOKING_BUTTON_XPATH)
    enter_class_button = PageElement(xpath=ENTER_CLASS_BUTTON_XPATH)

    def __init__(self, driver):
		AbstractBaseEvcAndroidPage.__init__(self, driver);

    def is_target_page(self):
        return self.is_element_displayed(By.XPATH, self.BOOKING_BUTTON_XPATH)

    def enter_class(self, enter_class_text=u"进入教室 "):
        while True: #Need to refine this function later
            status = self.enter_class_button.get_attribute("name")
            if status == enter_class_text:
                break
            else:
                pass
        self.enter_class_button.click()
        return EvcRoomPage(self.driver)

if __name__ == '__main__':
	pass
