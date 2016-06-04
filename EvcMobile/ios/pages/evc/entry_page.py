from random import randint

from page_objects import PageElement

import settings
from ios.pages.evc.abstract_base_evc_ios_page import AbstractBaseEvcIosPage
from ios.pages.evc.classroom_page import ClassroomPage


class EntryPage(AbstractBaseEvcIosPage):

    YOUR_NAME_FIELD_XPATH = "//UIAStaticText[@name='YOUR NAME']/following-sibling::UIATextField[1]"
    ROOM_NAME_FIELD_XPATH = "//UIAStaticText[@name='ROOM NAME']/following-sibling::UIATextField[1]"
    CONTENT_ID_DROPDOWN_LIST_XPATH = "//UIAStaticText[@name='CONTENT ID']/following-sibling::UIAElement[1]"
    CONTENT_ID_PICKER_WHEEL_XPATH = "//UIAPickerWheel"
    DURATION_FIELD_XPATH = "//UIAStaticText[@name='DURATION (MINS)']/following-sibling::UIATextField[1]"
    JOIN_BUTTON_XPATH = "//UIAButton[contains(@name, 'JOIN')]"

    your_name_field = PageElement(xpath=YOUR_NAME_FIELD_XPATH)
    room_name_field = PageElement(xpath=ROOM_NAME_FIELD_XPATH)
    content_id_dropdown_list = PageElement(xpath=CONTENT_ID_DROPDOWN_LIST_XPATH)
    duration_field = PageElement(xpath=DURATION_FIELD_XPATH)
    join_button = PageElement(xpath=JOIN_BUTTON_XPATH)
    content_id_picker_wheel = PageElement(xpath=CONTENT_ID_PICKER_WHEEL_XPATH)

    def is_target_page(self):
        return self.is_element_exist(self.YOUR_NAME_FIELD_XPATH)

    def set_your_name(self, your_name):
        self.your_name_field.clear()
        self.your_name_field.send_keys(your_name)

    def set_room_name(self, room_name):
        self.room_name_field.clear()
        self.room_name_field.send_keys(room_name)

    def select_content_id(self, content_id):
        self.content_id_dropdown_list.click()
        self.content_id_picker_wheel.send_keys(content_id)

    def set_duration(self, duration):
        self.duration_field.clear()
        self.duration_field.send_keys(duration)

    def click_join_button(self):
        self.join_button.click()

    def enter_class_room(self, teacher_name=settings.TEACHER_NAME_1, room_name=None, content_id=None, duration=None):
        self.set_your_name(teacher_name)

        if room_name:
            self.room_name = room_name
        else:
            self.room_name = 'ROOM_' + str(randint(0, 9999)).rjust(4, '0')
        self.set_room_name(self.room_name)

        if content_id:
            self.select_content_id(content_id)

        if duration:
            self.set_duration(duration)

        self.click_join_button()

        return ClassroomPage(self.driver)
