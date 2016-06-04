import time

import settings
from evc15.evc15_common import utilities
from evc15.evc15_common.header.check_type import CheckType

__author__ = 'Alice.Sun'


class Attendees(object):
    HOST_ICON_XPATH = "//span[@class='icon-teacher']"
    CLASSROOM_LOGO_XPATH = "//span[@class='evc-logo']"

    HOST_NAME_XPATH = "//div[@class='hosts']//span[@class='name']"
    STUDENT_NAME_XPATH = "(//div[@class='non-hosts']//div[@class='name'])[%s]"

    AUDIO_STATUS_XPATH = "//button[@title='Turn on/off microphone']"
    VIDEO_STATUS_XPATH = "//button[@title='Turn on/off camera']"

    OTHER_STUDENT_AUDIO_STATUS_XPATH = "//div[@class='non-hosts']/div[@class='user ']//div[@class='toggles']/span[1]"
    OTHER_STUDENT_VIDEO_STATUS_XPATH = "//div[@class='non-hosts']/div[@class='user ']//div[@class='toggles']/span[2]"

    HOSTS_DIV_XPATH = "//div[@class='users-container']/div[@class='hosts']"
    NON_HOSTS_DIV_XPATH = "//div[@class='users-container']/div[@class='non-hosts']"

    RAISE_HAND_BUTTON_XPATH = "//div[@class='toggles']/span[@class[contains(.,'icon-raise-hand')]]"

    def __init__(self, browser=""):
        self.browser = browser

    def check_host_icon_exists(self):
        self.browser.find_element_by_xpath(self.HOST_ICON_XPATH)

    def verify_enter_classroom_successfully(self):
        if utilities.element_exists(self.browser, self.CLASSROOM_LOGO_XPATH):
            self.browser.find_element_by_xpath(self.CLASSROOM_LOGO_XPATH)

    def check_host_name(self, expected_host_name):
        actual_name = self.browser.find_element_by_xpath(self.HOST_NAME_XPATH).text
        # Change Unicode to String
        str_actual_name = str(actual_name)
        utilities.are_equal("Host name", expected_host_name, str_actual_name)

    def check_host_audio_status(self, audio_status):
        actual_audio_status = str(
                self.browser.find_element_by_xpath(self.AUDIO_STATUS_XPATH).get_attribute("class"))
        utilities.are_equal("Audio status", audio_status, actual_audio_status)

    def check_host_video_status(self, video_status):
        actual_video_status = str(
                self.browser.find_element_by_xpath(self.VIDEO_STATUS_XPATH).get_attribute("class"))
        utilities.are_equal("Video status", video_status, actual_video_status)

    def check_student_name(self, expected_student_name, number):
        actual_student_name = self.browser.find_element_by_xpath(self.STUDENT_NAME_XPATH % number).get_attribute(
                "title")
        str_actual_student_name = str(actual_student_name)
        utilities.are_equal("The name of student %s" % number, expected_student_name, str_actual_student_name)

    def check_student_audio_status(self, check_type, expected_audio_status):
        elapsed_time = 0
        current_student_audio_status_flag = False

        while elapsed_time < settings.FIND_ELEMENT_TIMEOUT:
            if check_type == CheckType.Current_Student_Check_Himself:
                xpath = self.AUDIO_STATUS_XPATH
            else:
                xpath = self.OTHER_STUDENT_AUDIO_STATUS_XPATH

            if expected_audio_status != str(
                    self.browser.find_element_by_xpath(xpath).get_attribute("class")):
                time.sleep(settings.DEFAULT_SLEEP_TIME)
                elapsed_time += settings.DEFAULT_SLEEP_TIME
                continue
            else:
                current_student_audio_status_flag = True
                break

        if current_student_audio_status_flag is False:
            raise AssertionError("Check current student audio status failed!")

    def check_student_video_status(self, check_type, expected_video_status):
        elapsed_time = 0
        current_student_video_status_flag = False

        while elapsed_time < settings.FIND_ELEMENT_TIMEOUT:
            if check_type == CheckType.Current_Student_Check_Himself:
                xpath = self.VIDEO_STATUS_XPATH
            else:
                xpath = self.OTHER_STUDENT_VIDEO_STATUS_XPATH

            if expected_video_status != str(
                    self.browser.find_element_by_xpath(xpath).get_attribute("class")):
                time.sleep(settings.DEFAULT_SLEEP_TIME)
                elapsed_time += settings.DEFAULT_SLEEP_TIME
                continue
            else:
                current_student_video_status_flag = True
                break

        if current_student_video_status_flag is False:
            raise AssertionError("Check current student video status failed!")

    def verify_support_invisible(self):
        hosts_div = self.browser.find_element_by_xpath(self.HOSTS_DIV_XPATH)
        non_hosts_div = self.browser.find_element_by_xpath(self.NON_HOSTS_DIV_XPATH)
        assert hosts_div.text == "", "Support is expected to be invisible, but not."
        assert non_hosts_div.text == "", "Support is expected to be invisible, but not."

    def click_mute_host_audio_button(self):
        audio_button = self.browser.find_element_by_xpath(self.AUDIO_STATUS_XPATH)
        audio_button.click()

    def click_disable_host_video_button(self):
        video_button = self.browser.find_element_by_xpath(self.VIDEO_STATUS_XPATH)
        video_button.click()

    def click_mute_student_audio_button(self, side):
        if side == "teacher_mute_student":
            xpath = self.OTHER_STUDENT_AUDIO_STATUS_XPATH
        else:
            xpath = self.AUDIO_STATUS_XPATH

        if utilities.element_exists(self.browser, xpath):
            audio_button = self.browser.find_element_by_xpath(xpath)
            audio_button.click()

    def click_disable_student_video_button(self, side):
        if side == "teacher_disable_student":
            xpath = self.OTHER_STUDENT_VIDEO_STATUS_XPATH
        else:
            xpath = self.VIDEO_STATUS_XPATH

        if utilities.element_exists(self.browser, xpath):
            video_button = self.browser.find_element_by_xpath(xpath)
            video_button.click()

    def check_raise_hand_button_show_in_attendee_list(self):
        self.browser.find_element_by_xpath(self.RAISE_HAND_BUTTON_XPATH)

    def click_low_down_hand_of_current_student(self):
        hand_button_of_current_student = self.browser.find_element_by_xpath(self.RAISE_HAND_BUTTON_XPATH)
        hand_button_of_current_student.click()
