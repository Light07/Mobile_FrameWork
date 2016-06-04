#encoding:utf-8

import os
from abc import ABCMeta

import settings
from common.appium_for_android_utils import AppiumUtils
from common.device_factory import DeviceFactory
from common.file_utils import FileUtils
from ef_common.frontend_testcase import FrontEndTestCase
from ef_common.seleniumhelper import SeleniumHelper

class AbstractBaseAndroidTestCase(FrontEndTestCase):

    __metaclass__ = ABCMeta

    def __init__(self):

        AppiumUtils.start_adb()
        AppiumUtils.launch_appium()

        self.app = os.path.abspath(FileUtils.get_apps_path() + os.path.sep + settings.APP_NAME)

        device = DeviceFactory.get_device_by_name(settings.ANDROID_DEVICE_NAME)

        self.capability = {
            'apps': self.app,
            'deviceName': device.get_device_name(),
            'platformName': device.get_platform_name(),
            'platformVersion': device.get_platform_version(),
            'unicodeKeyboard': True,
            'resetKeyboard': True
        }

        self.appium_server_ip = settings.APPIUM_SERVER_IP
        self.appium_server_port = settings.APPIUM_SERVER_PORT

    def create_browser_driver(self):
        self.browser = SeleniumHelper.open_browser(self, browser_name="device")

    def close_browser(self):
        try:
            self.browser.quit()
        except Exception as err:
            print err
        finally:
            AppiumUtils.close_appium()