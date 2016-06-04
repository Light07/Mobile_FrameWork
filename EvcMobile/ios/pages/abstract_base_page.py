#encoding:utf-8

import time

from abc import ABCMeta, abstractmethod
from DateTime import DateTime
from hamcrest import assert_that
from hamcrest import equal_to
from page_objects import PageObject
from selenium.common.exceptions import NoSuchElementException

from common import date_time_utils
import settings

class AbstractBasePage(PageObject):

    __metaclass__ = ABCMeta

    WAIT_FOR_SCROLL_TIME = 2

    def __init__(self, driver):
        # Don't change the variable name w. it's used by PageObject
        self.w = driver
        self.driver = driver
        assert_that(self.has_loaded(), equal_to(True), self.__class__.__name__ + ' is not load!')

    def has_loaded(self):
        try:
            return self.is_target_page()
        except NoSuchElementException:
            return False

    # This function will be implement by sub class
    @abstractmethod
    def is_target_page(self):
        pass

    def is_element_exist(self, xpath, timeout=settings.IMPLICITLY_WAIT_TIME):
        start_time = DateTime()
        is_found = False

        time.sleep(settings.SLEEP_INTERVAL)
        while date_time_utils.get_diff_in_seconds(start_time, DateTime()) < timeout:
            if len(self.driver.find_elements_by_xpath(xpath)) > 0:
                is_found = True
                break

            time.sleep(settings.SLEEP_INTERVAL)

        return is_found

    def is_text_displayed(self, text):
        xpath = "//UIAStaticText[@label='" + text + "']"

        return self.is_element_exist(xpath)
