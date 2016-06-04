#encoding:utf-8
from hamcrest import equal_to, assert_that

from settings.environment import UAT_Account
from ef_common.take_screenshot import take_screenshot
from android.pages.evc.login_page import LoginPage
from android.tests.abstract_base_android_testcase import AbstractBaseAndroidTestCase

class TestStudentEnterEvcClassOnDebugMode(AbstractBaseAndroidTestCase):
    @take_screenshot
    def runTest(self):
        username =UAT_Account.EFEC_BEG_IN_WHITE_LIST_Account['username']
        login_page = LoginPage(self.browser)
        debug_page = login_page.go_to_debug_option_page()
        class_room_entry_page = debug_page.go_to_class_room_entry_page()
        room_name = class_room_entry_page.get_class_room_name()
        evc_class = class_room_entry_page.go_to_evc_room(username, room_name)
        evc_class.select_chat_button()
        evc_class.send_text_through_chat_dialog(48)

if __name__ == '__main__':
    test = TestStudentEnterEvcClassOnDebugMode()
    test.create_browser_driver()
    test.runTest()
    test.close_browser()