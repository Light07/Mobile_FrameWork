#encoding:utf-8

import time

from abc import ABCMeta, abstractmethod
from DateTime import DateTime
from hamcrest import assert_that
from hamcrest import equal_to
from page_objects import PageObject, PageElement
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common import common_expected_conditions
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

    def is_element_displayed(self, by, value, timeout=settings.TIMEOUT):
        return WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(by, value).is_displayed())

    def is_element_displayed_on_page(self, ele, timeout=settings.TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(lambda driver: ele.is_displayed())
            result = True
        except Exception, e:
            result = False
        return result

    def is_element_exists(self, xpath):
        size = -1
        size = len(self.driver.find_elements_by_xpath(xpath))
        if size > 0:
            return True
        else:
            return False

    def is_equal(assert_object, expect, actual):
        assert expect == actual, \
            ("%s is not match. Expect: %s, Actual: %s" % (assert_object, expect, actual))

    def is_page_loaded(self, target_url_string, time_out=settings.TIMEOUT):
        time_waited = 0
        status = False

        while (time_waited < time_out):
            url = self.driver.current_url
            if target_url_string in url:
                status = True
                break
            else:
                time.sleep(settings.SLEEP_INTERVAL)
                time_waited += settings.SLEEP_INTERVAL

        return status