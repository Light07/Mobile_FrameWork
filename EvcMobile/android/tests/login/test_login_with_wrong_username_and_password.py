#encoding:utf-8

from hamcrest import assert_that, equal_to

from settings.environment import UAT_Account
from ef_common.take_screenshot import take_screenshot
from android.pages.evc.login_page import LoginPage
from android.tests.abstract_base_android_testcase import AbstractBaseAndroidTestCase

class TestLoginWithWrongUsernameAndPassword(AbstractBaseAndroidTestCase):
    @take_screenshot
    def runTest(self):
        login_page = LoginPage(self.browser)
        login_page.set_username_or_email(UAT_Account.EFEC_Invalid_Account["username"])
        login_page.set_password(UAT_Account.EFEC_Invalid_Account["password"])
        login_page.click_login_button()
        assert_that(login_page.error_message.get_attribute("name").encode('utf-8'), equal_to('未注册的用户名或者密码错误'))

if __name__ == '__main__':
    test = TestLoginWithWrongUsernameAndPassword()
    test.create_browser_driver()
    test.runTest()
    test.close_browser()