import settings
from android.pages.abstract_base_page import AbstractBasePage


class AbstractBaseEvcAndroidPage(AbstractBasePage):

    def __init__(self, driver):
        AbstractBasePage.__init__(self, driver)
        self.driver.implicitly_wait(settings.IMPLICITLY_WAIT_TIME)

    def get_screen_resolution(self):
        return self.driver.get_window_size()

    def get_screen_center_location(self):
        x = self.get_screen_resolution().get('width') / 2
        y = self.get_screen_resolution().get('height') / 2
        return {'width':x, 'height':y}