from ef_common.take_screenshot import take_screenshot
from hamcrest import assert_that, equal_to

import settings
from android.pages.evc.login_page import LoginPage
from settings import UAT_Account
from teacher_common.teacher_common_web_page import TeacherCommonWebPage
from android.tests.abstract_base_android_testcase import AbstractBaseAndroidTestCase

class TestChats(AbstractBaseAndroidTestCase):

    @take_screenshot
    def runTest(self):
        # Student enter class.
        student_name =UAT_Account.EFEC_BEG_IN_WHITE_LIST_Account['username']
        login_page = LoginPage(self.browser)
        debug_page = login_page.go_to_debug_option_page()
        class_room_entry_page = debug_page.go_to_class_room_entry_page()
        room_name = class_room_entry_page.get_class_room_name()
        duration_time = class_room_entry_page.get_class_room_duration()
        evc_class = class_room_entry_page.go_to_evc_room(student_name, room_name)
        # Student send message
        evc_class.select_chat_button()
        evc_class.send_text_through_chat_dialog(33)

        # Teacher enter class
        teacher_name = settings.TEACHER_NAME_1
        evc_room = TeacherCommonWebPage()
        evc_room.join_specific_class_room(teacher_name, room_name=room_name, duration=duration_time)
        evc_room.chat.send_chat_messages("T")
        #  Verify the message sent by student.
        evc_room.chat.get_messages_by_user_name(student_name)
        assert_that(evc_room.chat.get_messages_by_user_name(student_name)[0], equal_to('e'))

if __name__ == "__main__":
    test = TestChats()
    test.create_browser_driver()
    test.runTest()
    test.close_browser()