from time import sleep

import settings
from selenium.webdriver.support.select import Select
from page_objects import PageElement
from evc15.evc15_common.abstract_base_page import AbstractBasePage
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


class JoinPage(AbstractBasePage):
    PAGE_TITLE_ID = "Trick"
    ADVANCED_SETTINGS_ID = "spanCbx"

    USER_INPUT_NAME = "UserDisplayName"
    ROOM_INPUT_NAME = "RoomName"
    JOIN_BUTTON_NAME = "Create"
    ROLE_SELECTOR_NAME = "RoleSelection"
    PPT_SELECTOR_NAME = "ContentId"
    DURATION_INPUT_NAME = "Duration"
    TECH_CHECK_CHECKBOX_NAME = "EnableTechCheck"

    CURRENT_PAGE_URL = settings.WEB_ROOT
    DEFAULT_MEETING_DURATION = 5

    page_title_label = PageElement(id_=PAGE_TITLE_ID)
    user_input = PageElement(name=USER_INPUT_NAME)
    room_input = PageElement(name=ROOM_INPUT_NAME)
    duration_input = PageElement(name=DURATION_INPUT_NAME)
    join_button = PageElement(name=JOIN_BUTTON_NAME)
    tech_check_checkbox = PageElement(name=TECH_CHECK_CHECKBOX_NAME)
    role_selector = PageElement(name=ROLE_SELECTOR_NAME)
    ppt_selector = PageElement(name=PPT_SELECTOR_NAME)
    advanced_settings_span = PageElement(id_=ADVANCED_SETTINGS_ID)

    def __init__(self, browser=""):
        self.browser = browser
        # Don't change the variable name w. it's used by PageObject
        self.w = browser

    def is_target_page(self):
        if self.is_page_loaded(self.CURRENT_PAGE_URL) and self.is_element_displayed(By.ID, self.PAGE_TITLE_ID):
            return True
        else:
            return False

    def get(self):
        self.browser.get(self.CURRENT_PAGE_URL)

    def set_user_name(self, user_name):
        self.user_input.clear()
        self.user_input = user_name

    def set_room_name(self, room_name):
        self.room_input.clear()
        self.room_input = room_name

    def select_by_visible_text(self, element, text):
        select = Select(element)
        select.select_by_visible_text(text)

    def select_user_role(self, role_name):
        if not self.element_displayed(self.role_selector):
            ActionChains(self.browser).double_click(self.page_title_label).perform()

        self.select_by_visible_text(self.role_selector, role_name)

    def select_ppt_name(self, ppt_name):
        if not self.element_displayed(self.ppt_selector):
            ActionChains(self.browser).double_click(self.page_title_label).perform()

        self.select_by_visible_text(self.ppt_selector, ppt_name)

    def set_duration(self, duration):
        if not self.element_displayed(self.duration_input):
            ActionChains(self.browser).double_click(self.page_title_label).perform()

        self.duration_input.clear()
        self.duration_input = duration

    def get_all_ppt_names(self):
        if not self.element_displayed(self.ppt_selector):
            ActionChains(self.browser).double_click(self.page_title_label).perform()

        ppt_names = []
        all_options = self.ppt_selector.find_elements_by_tag_name("option")
        for option in all_options:
            ppt_names.append(option.get_attribute("value"))

        return ppt_names

    """
    :duration: unit is minute
    :default_sleep: second, because demo page join meeting function has a known concurrency issue
    """

    def join_meeting(self, user_name, role_name, room_name=None, duration=None, ppt_name=None, default_sleep=None):
        if default_sleep is not None:
            sleep(default_sleep)

        self.get()
        self.set_user_name(user_name)

        if room_name is not None:
            self.set_room_name(room_name)

        room_name = self.room_input.get_attribute("value")

        if duration is None:
            duration = self.DEFAULT_MEETING_DURATION

        self.set_duration(duration)
        self.select_user_role(role_name)

        if ppt_name is not None:
            self.select_ppt_name(ppt_name)

        self.join_button.click()
        return room_name
