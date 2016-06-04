import time
import settings
from page_objects import PageElement, MultiPageElement
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from evc15.evc15_common.abstract_base_page import AbstractBasePage


class Chat(AbstractBasePage):
    CHAT_TITLE_CSS = ".nc-chat .name"
    CHAT_INPUT_CSS = ".nc-chat .nc-keyboard-input"
    CHAT_MESSAGES_CSS = ".nc-chat .messages li"

    SELF_MESSAGES_FLAG = "myself"
    OTHERS_MESSAGES_FLAG = "others"
    SOFT_HYPHEN = u'\xad'
    CHAT_SEPARATOR = u':\n'

    chat_title_label = PageElement(css=CHAT_TITLE_CSS)
    chat_input = PageElement(css=CHAT_INPUT_CSS)
    chat_messages = MultiPageElement(css=CHAT_MESSAGES_CSS)

    def __init__(self, browser=""):
        AbstractBasePage.__init__(self, browser)

    def is_target_page(self):
        if self.is_element_displayed(By.CSS_SELECTOR, self.CHAT_TITLE_CSS):
            return True
        else:
            return False

    def clean_chat_input(self):
        self.chat_input.clear()

    def send_chat_messages(self, messages):
        for message in messages:
            self.chat_input.send_keys(message)
            self.chat_input.send_keys(Keys.ENTER)

    def is_page_display_all_messages(self, expected_number):
        elapsed_time = 0
        while elapsed_time < settings.FIND_ELEMENT_TIMEOUT:
            if len(self.chat_messages) != expected_number:
                elapsed_time += settings.DEFAULT_SLEEP_TIME
                time.sleep(settings.DEFAULT_SLEEP_TIME)
            else:
                return True
        return False

    def get_meeting_messages(self):
        self_messages, others_messages = self.get_messages_with_sender_name()
        self_result, others_result = [], []

        for self_message in self_messages:
            self_result.append(self_message.split(self.CHAT_SEPARATOR)[1])

        for others_message in others_messages:
            others_result.append(others_message.split(self.CHAT_SEPARATOR)[1])

        return self_result, others_result

    def get_messages_with_sender_name(self):
        self_result, others_result = [], []

        for chat_message in self.chat_messages:
            if self.SELF_MESSAGES_FLAG in chat_message.get_attribute("class"):
                message = chat_message.text.replace(self.SOFT_HYPHEN, '').strip()
                self_result.append(message)
            elif self.OTHERS_MESSAGES_FLAG in chat_message.get_attribute("class"):
                message = chat_message.text.replace(self.SOFT_HYPHEN, '').strip()
                others_result.append(message)

        return self_result, others_result

    def is_messages_sent_by_user(self, messages_with_sender_name, user_name):
        for message in messages_with_sender_name:
            sender_name = message.split(self.CHAT_SEPARATOR)[0]

            if sender_name == user_name:
                continue
            else:
                return False

        return True

    def get_messages_by_user_name(self, user_name):
        result = []

        for chat_message in self.chat_messages:
            message = chat_message.text.replace(self.SOFT_HYPHEN, '').strip()

            if message.split(self.CHAT_SEPARATOR)[0] == user_name:
                result.append(message.split(self.CHAT_SEPARATOR)[1])

        return result