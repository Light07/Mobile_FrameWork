#encoding:utf-8
from ef_common.take_screenshot import take_screenshot
from hamcrest import assert_that

from ios.pages.evc import LoginPage
from ios.tests.abstract_base_ios_testcase import AbstractBaseIosTestCase


class TestLoginWithWrongUsernameAndPassword(AbstractBaseIosTestCase):

    @take_screenshot
    def runTest(self):
        login_page = LoginPage(self.browser)

        login_page.set_username_or_email("tails82@sohu.com")
        login_page.set_password("bbb")
        login_page.click_login_button()
        login_page.waitForAppProgress()

        assert_that(login_page.is_text_present('未注册的用户名或者密码错误'), equal_to(True))

if __name__ == '__main__':
    test = TestLoginWithWrongUsernameAndPassword()
    test.create_browser_driver()
    test.runTest()
    test.close_browser()
