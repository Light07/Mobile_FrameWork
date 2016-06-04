import time
import settings
from evc15.evc15_common import utilities


class Header(object):
    MICROPHONE_BUTTON_XPATH = "//button[@title='Toggle microphone']"
    MICROPHONE_BUTTON_STATUS_XPATH = "//button[@title='Toggle microphone']/i"
    CAMERA_BUTTON_XPATH = "//button[@title='Toggle camera']"
    CAMERA_BUTTON_STATUS_XPATH = "//button[@title='Toggle camera']/i"
    RAISE_HAND_BUTTON_XPATH = "//button[@title='Raise hand']"
    RAISE_HAND_BUTTON_STATUS_XPATH = "//button[@title='Raise hand']/i"

    def __init__(self, browser=""):
        self.browser = browser

    def click_raise_hand_button(self):
        if utilities.element_exists(self.browser, self.RAISE_HAND_BUTTON_XPATH):
            self.browser.find_element_by_xpath(self.RAISE_HAND_BUTTON_XPATH).click()

    def check_raise_hand_button_status(self, expected_raise_hand_button_status):
        elapsed_time = 0
        raise_hand_button_status_flag = False
        while elapsed_time < settings.FIND_ELEMENT_TIMEOUT:
            if expected_raise_hand_button_status != str(
                    self.browser.find_element_by_xpath(self.RAISE_HAND_BUTTON_STATUS_XPATH).get_attribute("class")):
                time.sleep(settings.DEFAULT_SLEEP_TIME)
                elapsed_time += settings.DEFAULT_SLEEP_TIME
                continue
            else:
                raise_hand_button_status_flag = True
                break

        if raise_hand_button_status_flag is False:
            raise Exception("Check raise hand button status failed!")

    def check_header_audio_status(self, audio_status):
        elapsed_time = 0
        header_audio_status_flag = False
        while elapsed_time < settings.FIND_ELEMENT_TIMEOUT:
            try:
                actual_audio_status = str(
                        self.browser.find_element_by_xpath(self.MICROPHONE_BUTTON_STATUS_XPATH).get_attribute("class"))
                assert audio_status == actual_audio_status
                header_audio_status_flag = True
                break
            except Exception:
                time.sleep(settings.DEFAULT_SLEEP_TIME)
                elapsed_time += settings.DEFAULT_SLEEP_TIME
                continue

        if header_audio_status_flag is False:
            raise Exception

    def check_header_video_status(self, video_status):
        elapsed_time = 0
        header_video_status_flag = False
        while elapsed_time < settings.FIND_ELEMENT_TIMEOUT:
            try:
                actual_video_status = str(
                        self.browser.find_element_by_xpath(self.CAMERA_BUTTON_STATUS_XPATH).get_attribute("class"))
                assert video_status == actual_video_status
                header_video_status_flag = True
                break
            except Exception:
                time.sleep(settings.DEFAULT_SLEEP_TIME)
                elapsed_time += settings.DEFAULT_SLEEP_TIME
                continue

        if header_video_status_flag is False:
            raise Exception

    def click_mute_audio_button(self):
        audio_button = self.browser.find_element_by_xpath(self.MICROPHONE_BUTTON_XPATH)
        audio_button.click()

    def click_disable_video_button(self):
        video_button = self.browser.find_element_by_xpath(self.CAMERA_BUTTON_XPATH)
        video_button.click()
