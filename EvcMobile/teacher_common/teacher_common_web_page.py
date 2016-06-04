from ef_common.seleniumhelper import SeleniumHelper
from evc15.evc15_common.attendee_list.attendees import Attendees
from evc15.evc15_common.chat.chat import Chat
from evc15.evc15_common.header.check_type import CheckType
from evc15.evc15_common.header.header import Header
from evc15.evc15_common.join.joinpage import JoinPage
from evc15.evc15_common.join.role import Role
from android.pages.evc.class_room_entry_page import ClassRoomEntryPage

class TeacherCommonWebPage(object):
    def __init__(self):
        self.driver = SeleniumHelper.open_browser()
        self.join_page = JoinPage(self.driver)
        self.attendees = Attendees(self.driver)
        self.chat = Chat(self.driver)

    def join_specific_class_room(self, user_name, role_name=Role.Host, room_name=None, duration=None, ppt_name=None, default_sleep=None):
        host_join_page = self.join_page
        host_join_page.join_meeting(user_name, role_name, room_name, duration, ppt_name, default_sleep)

        attendees = self.attendees
        attendees.verify_enter_classroom_successfully()

    def get_chat_message(self):
        chat = self.chat
        return chat.get_meeting_messages()


    def __del__(self):
        self.driver.close()