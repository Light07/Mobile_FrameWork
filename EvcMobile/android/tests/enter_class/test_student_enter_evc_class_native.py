#encoding:utf-8
from hamcrest import equal_to, assert_that

from settings.environment import UAT_Account
from ef_common.take_screenshot import take_screenshot
from android.pages.evc.login_page import LoginPage
from android.tests.abstract_base_android_testcase import AbstractBaseAndroidTestCase

class TestStudentEnterEvcClass(AbstractBaseAndroidTestCase):
    @take_screenshot
    def runTest(self):
        login_page = LoginPage(self.browser)
        username =UAT_Account.EFEC_BEG_IN_WHITE_LIST_Account['username']
        password = UAT_Account.EFEC_BEG_IN_WHITE_LIST_Account['password']
        my_booking_page = login_page.login(username, password)
        assert_that(my_booking_page.is_element_displayed_on_page(my_booking_page.book_button), equal_to(True))

        evc_class = my_booking_page.enter_class()
        evc_class.select_chat_button()
        evc_class.send_text_through_chat_dialog(48)

if __name__ == '__main__':
    test = TestStudentEnterEvcClass()
    test.create_browser_driver()
    test.runTest()
    test.close_browser()