from ef_common.take_screenshot import take_screenshot
from hamcrest import assert_that

from ios.pages.evc.entry_page import EntryPage
from ios.tests.abstract_base_ios_testcase import AbstractBaseIosTestCase


class TestSendChatMessage(AbstractBaseIosTestCase):

    @take_screenshot
    def runTest(self):

        entry_page = EntryPage(self.browser)
        classroom_page = entry_page.enter_class_room()
        classroom_page.expand_side_menu()
        classroom_page.click_chat_icon()
        classroom_page.set_send_message('hello')
        classroom_page.send_chat_message()

        assert_that(classroom_page.is_text_displayed('hello'))

if __name__ == '__main__':
    test = TestSendChatMessage()
    test.create_browser_driver()
    test.runTest()
    test.close_browser()
