import time

from abc import ABCMeta, abstractmethod
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import settings


class AbstractBasePage(object):
    __metaclass__ = ABCMeta

    def __init__(self, browser):
        self.browser = browser
        # Don't change the variable name w. it's used by PageObject
        self.w = browser

    # This function will be implement by sub class
    @abstractmethod
    def is_target_page(self):
        pass

    def is_element_displayed(self, by, value):
        return WebDriverWait(self.browser, settings.FIND_ELEMENT_TIMEOUT).until(
                lambda driver: driver.find_element(by, value).is_displayed())

    def element_displayed(self, element):
        try:
            status = element.is_displayed()
        except Exception:
            status = False
        return status

    def is_element_found(self, *by):
        try:
            if WebDriverWait(self.browser, settings.FIND_ELEMENT_TIMEOUT).until(EC.presence_of_element_located(by)):
                status = True
        except Exception:
            status = False
        return status

    def is_element_enabled(self, *by):
        try:
            if WebDriverWait(self.browser, settings.FIND_ELEMENT_TIMEOUT).until(
                    lambda driver: EC._find_element(driver, by)).is_enabled():
                status = True
            else:
                status = False
        except Exception:
            status = False
        return status

    def is_element_disabled(self, ele):
        status = False
        if ele.get_attribute("disabled") == 'true':
            status = True
        return status

    def wait_until_element_clickable(self, *by):
        WebDriverWait(self.browser, settings.TESTCASE_TIMEOUT).until(EC.element_to_be_clickable(by))

    def is_page_element_clickable(self, element, time_out=settings.TESTCASE_TIMEOUT):
        try:
            result = WebDriverWait(self.browser, time_out).until(
                    lambda driver: element.is_enabled() & element.is_displayed())
        except Exception:
            result = False
        return result

    def wait_until_element_disappear(self, xpath_locator, time_out=settings.TESTCASE_TIMEOUT):
        time_waited = 0
        while (time_waited < time_out):
            loading_element = self.element_displayed(xpath_locator)
            if (loading_element == False):
                break
            else:
                time.sleep(settings.SEARCH_POLL_TIME)
                time_waited += settings.SEARCH_POLL_TIME

    def is_page_loaded(self, target_url_string, time_out=settings.FIND_ELEMENT_TIMEOUT):
        time_waited = 0
        status = False

        while (time_waited < time_out):
            url = self.browser.current_url
            if target_url_string in url:
                status = True
                break
            else:
                time.sleep(settings.DEFAULT_SLEEP_TIME)
                time_waited += settings.DEFAULT_SLEEP_TIME

        return status
