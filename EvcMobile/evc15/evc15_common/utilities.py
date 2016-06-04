'''
Created on Dec 13, 2013

@author: lin.wang
'''

import time
import calendar
import datetime
import win32api
import settings
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


def get_option_text_list(browser, xpath):
    select = browser.find_element_by_xpath(xpath)
    allOptions = select.find_elements_by_tag_name("option")
    option_text_list = []
    for option in allOptions:
        option_text_list.append(option.text)
    return option_text_list


def verify_expected_text_in_list(text_list, expect_text_list, isInculded=True):
    for text in expect_text_list:
        assert text_list.__contains__(text) == isInculded, "The expected value %s isn't showed." % text


def element_exists(browser, xpath):
    exist_flag = False
    elapsed_time = 0
    # FIND_ELEMENT_TIMEOUT = 20 and settings.DEFAULT_SLEEP_TIME = 1 which defined in settings module
    while (elapsed_time < settings.FIND_ELEMENT_TIMEOUT) and (exist_flag is False):
        try:
            element = browser.find_element_by_xpath(xpath)
            # sometimes even the element can be found by xpath success, but it still in "NotVisible" Status,
            # here to make sure the element is visible
            if element.is_displayed() is False:
                time.sleep(settings.DEFAULT_SLEEP_TIME)
                elapsed_time += settings.DEFAULT_SLEEP_TIME
                continue
            exist_flag = True
        except NoSuchElementException:
            time.sleep(settings.DEFAULT_SLEEP_TIME)
            elapsed_time += settings.DEFAULT_SLEEP_TIME

    return exist_flag


def element_text_changed(browser, xpath, text):
    exist_flag = False
    elapsed_time = 0
    # FIND_ELEMENT_TIMEOUT = 20 and settings.DEFAULT_SLEEP_TIME = 1 which defined in settings module
    while (elapsed_time < settings.FIND_ELEMENT_TIMEOUT) and (exist_flag is False):
        browser.refresh()
        element = browser.find_element_by_xpath(xpath)
        # sometimes even the element can be found by xpath success, but it still in "NotVisible" Status,
        # here to make sure the element text is correct
        if element.text != text:
            time.sleep(settings.DEFAULT_SLEEP_TIME)
            elapsed_time += settings.DEFAULT_SLEEP_TIME
            continue
        else:
            exist_flag = True

    return exist_flag


def add_months(date_time, month):
    '''
    according our business logic, we need get the previous several months date.
    '''
    if month <= 0:
        if abs(month) <= 12:
            if date_time.month < abs(month):
                new_year = date_time.year - 1
                if abs(month) > 12:
                    new_year = date_time.year - (abs(month) % 12) - 1
                else:
                    new_year = date_time.year - 1
                new_month = date_time.month + 12 - abs(month)
                if new_month == 0:
                    new_month = 12
                    new_year -= 1
            else:
                new_year = date_time.year
                new_month = date_time.month - abs(month)
                if new_month == 0:
                    new_month = 12
                    new_year -= 1
        else:
            new_year = date_time.year - (abs(month) / 12)
            ex_m = abs(month) % 12
            if ex_m >= date_time.month:
                new_year -= 1
                new_month = date_time.month + 12 - ex_m
                if new_month == 0:
                    new_month = 12
                    new_year -= 1
            else:
                new_month = date_time.month - ex_m
                if new_month == 0:
                    new_month = 12
                    new_year -= 1
        if date_time.day > calendar.monthrange(new_year, new_month)[1]:
            new_day = calendar.monthrange(new_year, new_month)[1]
        else:
            new_day = date_time.day
        new_date_time = datetime.datetime(new_year, new_month, new_day)
        return new_date_time

    else:
        if date_time.month + month <= 12:
            new_month = date_time.month + month
            new_year = date_time.year
        else:
            new_year = date_time.year + (date_time.month + month) / 12
            new_month = (date_time.month + month) % 12
            if new_month == 0:
                new_month = 12
        if date_time.day > calendar.monthrange(new_year, new_month)[1]:
            new_day = calendar.monthrange(new_year, new_month)[1]
        else:
            new_day = date_time.day
        new_date_time = datetime.datetime(new_year, new_month, new_day)
        return new_date_time


def try_to_close_live_chat(browser):
    live_chat_xpath = "//img[@src[contains(.,'button_close')]]"
    time.sleep(settings.DEFAULT_SLEEP_TIME)
    try:
        browser.find_element_by_xpath(live_chat_xpath).click()
    except NoSuchElementException:
        pass


def wait_page_change(browser, current_page_url, timeout=30, sleep_time=settings.DEFAULT_SLEEP_TIME):
    elapsed_Time = 0
    while (browser.current_url == current_page_url):
        time.sleep(sleep_time)
        elapsed_Time = elapsed_Time + sleep_time
        if (elapsed_Time > timeout):
            raise Exception("The current cannot redirect to next web page.")


def move_mouse(x=0, y=0):
    """
    When simulating mouse movements with WebDriver, the actual mouse cursor on the screen does not move.
    Here use win32api to move mouse.
    You can download Python Win32 Extensions follow below url:
        http://starship.python.net/crew/mhammond/win32/Downloads.html
    Note:
        Should catch the Exception, because calls to SetCursorPos() fail when the workstation(VMs) is locked,
        that is designed for security feature.
    """
    try:
        win32api.SetCursorPos((x, y))
    except BaseException:
        pass


def wait_alert_show_up(browser, timeout=settings.TIMEOUT_FOR_ACTIVE):
    WebDriverWait(browser, timeout).until(EC.alert_is_present(), 'Timed out waiting for activate alert')
    try:
        alert = browser.switch_to_alert()
        alert.accept()
    except TimeoutException:
        assert False, "Cannot find alert!"


def are_equal(assert_object, expect, actual):
    assert expect == actual, \
        ("%s is not match. Expect: %s, Actual: %s" % (assert_object, expect, actual))
