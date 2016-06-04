from ef_common.take_screenshot import take_screenshot

from ios.pages.evc.entry_page import EntryPage
from ios.tests.abstract_base_ios_testcase import AbstractBaseIosTestCase


class TestEnterClassroom(AbstractBaseIosTestCase):

    @take_screenshot
    def runTest(self):
        entry_page = EntryPage(self.browser)
        entry_page = entry_page.enter_class_room(content_id='369')
        entry_page.expand_side_menu()
        entry_page.click_chat_icon()

if __name__ == '__main__':
    test = TestEnterClassroom()
    test.create_browser_driver()
    test.runTest()
    test.close_browser()