import os
import time

from DateTime import DateTime
from selenium.common.exceptions import TimeoutException

import settings
from common import date_time_utils
from common.device_factory import DeviceFactory
from common.file_utils import FileUtils

class AppiumForIOSUtils:

    WAIT_FOR_APPIUM_SERVER_STARTUP_TIMEOUT = 10
    WAIT_FOR_APPIUM_SERVER_STOP_TIMEOUT = 5
    DELAY_TIME_FOR_START_CLOSE_APPIUM = 2
    CHECK_APPIUM_STATUS_INTERVAL = 2
    WAIT_FOR_WEBKIT_DEBUG_PROXY_STARTUP_TIMEOUT = 10
    WAIT_FOR_WEBKIT_DEBUG_PROXY_STOP_TIMEOUT = 5
    CHECK_WEBKIT_DEBUG_PROXY_STATUS_INTERVAL = 2

    appium_thread = None

    @staticmethod
    def launch_appium():

        AppiumForIOSUtils.close_appium()
        AppiumForIOSUtils.close_ios_webkit_debug_proxy()

        AppiumForIOSUtils.generate_launch_command()

        command = (FileUtils.get_current_file_path(__file__) + os.path.sep + "start_appium_for_ios.sh").replace(' ', '\ ')

        os.system("%s" % command)

        # webkit_debug_proxy will be started only for real device
        device = DeviceFactory.get_device_by_name(settings.IOS_DEVICE_NAME)
        if device.get_udid() != '':
            AppiumForIOSUtils.wait_until_webkit_debug_proxy_start(AppiumForIOSUtils.WAIT_FOR_WEBKIT_DEBUG_PROXY_STARTUP_TIMEOUT)
        AppiumForIOSUtils.wait_until_appium_start(AppiumForIOSUtils.WAIT_FOR_APPIUM_SERVER_STARTUP_TIMEOUT)

    @staticmethod
    def generate_launch_command():
        device = DeviceFactory.get_device_by_name(settings.IOS_DEVICE_NAME)

        # For Simulator
        if device.get_udid() == '':
            command_template = FileUtils.read_from_file(FileUtils.get_current_file_path(__file__) + os.path.sep + "start_appium_for_ios_simulator_template.sh")

            command = command_template.format(settings.APPIUM_SERVER_IP, settings.APPIUM_SERVER_PORT,
                                              settings.COMMAND_TIMEOUT, device.get_platform_version(),
                                              device.get_platform_name(), FileUtils.get_apps_path() + os.path.sep + 'evc.app',
                                              device.get_udid(), device.get_device_name(), FileUtils.get_appium_log_file_path_for_ios().replace(' ', '\ '))
        # For real device
        else:
            command_template = FileUtils.read_from_file(FileUtils.get_current_file_path(__file__) + os.path.sep + "start_appium_for_ios_template.sh")

            command = command_template.format(device.get_udid(), settings.APPIUM_SERVER_IP, settings.APPIUM_SERVER_PORT,
                                              settings.COMMAND_TIMEOUT, device.get_platform_version(),
                                              device.get_platform_name(), FileUtils.get_apps_path() + os.path.sep + 'evc.app',
                                              device.get_udid(), device.get_device_name(), FileUtils.get_appium_log_file_path_for_ios().replace(' ', '\ '))

        f = open(FileUtils.get_current_file_path(__file__) + os.path.sep + "start_appium_for_ios.sh", 'w')
        f.write(command)
        f.close()

    @staticmethod
    def is_appium_start():
        result_stream = os.popen('ps aux | grep node')

        result = FileUtils.read_from_stream(result_stream.readlines())

        if settings.APPIUM_SERVER_IP in result:
            return True
        else:
            return False

    @staticmethod
    def wait_until_appium_start(timeout):
        start_time = DateTime()

        is_started = False
        has_log = False
        while (is_started == False or has_log == False) & (date_time_utils.get_diff_in_seconds(start_time, DateTime()) < timeout):
            time.sleep(AppiumForIOSUtils.CHECK_APPIUM_STATUS_INTERVAL)
            is_started = AppiumForIOSUtils.is_appium_start()
            has_log = AppiumForIOSUtils.is_appium_log_file_is_written()

        if(not is_started):
            raise TimeoutException('Appium server is not started in ' + str(timeout) + ' seconds')

    @staticmethod
    def is_appium_log_file_is_written():
        log = FileUtils.read_from_file(FileUtils.get_appium_log_file_path_for_ios())
        if settings.APPIUM_SERVER_IP in log:
            return True
        else:
            return False


    @staticmethod
    def wait_until_appium_stop(timeout):
        start_time = DateTime()

        is_closed = False
        while (is_closed is not True) & (date_time_utils.get_diff_in_seconds(start_time, DateTime()) < timeout):
            time.sleep(AppiumForIOSUtils.CHECK_APPIUM_STATUS_INTERVAL)
            is_closed = not AppiumForIOSUtils.is_appium_start()

        if(not is_closed):
            raise TimeoutException('Appiun server is not stoped in ' + str(timeout) + ' seconds')

    @staticmethod
    def close_appium():
        os.system('killall node')
        AppiumForIOSUtils.wait_until_appium_stop(AppiumForIOSUtils.WAIT_FOR_APPIUM_SERVER_STOP_TIMEOUT)

    @staticmethod
    def close_ios_webkit_debug_proxy():
        os.system('killall ios_webkit_debug_proxy')
        AppiumForIOSUtils.wait_until_webkit_debug_proxy_stop(AppiumForIOSUtils.WAIT_FOR_WEBKIT_DEBUG_PROXY_STOP_TIMEOUT)

    @staticmethod
    def wait_until_webkit_debug_proxy_stop(timeout):
        start_time = DateTime()

        is_closed = False
        while (is_closed is not True) & (date_time_utils.get_diff_in_seconds(start_time, DateTime()) < timeout):
            time.sleep(AppiumForIOSUtils.CHECK_WEBKIT_DEBUG_PROXY_STATUS_INTERVAL)
            is_closed = not AppiumForIOSUtils.is_webkit_debug_proxy_start()

        if(not is_closed):
            raise TimeoutException('webkit debug proxy server is not stoped in ' + str(timeout) + ' seconds')

    @staticmethod
    def is_webkit_debug_proxy_start():
        result_stream = os.popen('ps aux | grep ios_webkit_debug_proxy -u')

        result = FileUtils.read_from_stream(result_stream.readlines())

        device = DeviceFactory.get_device_by_name(settings.IOS_DEVICE_NAME)
        if device.get_udid() == "":
            if ':27753' in result:
                return True
            else:
                return False
        else:
            if device.get_udid() in result:
                return True
            else:
                return False

    @staticmethod
    def wait_until_webkit_debug_proxy_start(timeout):
        start_time = DateTime()

        is_started = False
        has_log = False
        while (is_started == False or has_log == False) & (date_time_utils.get_diff_in_seconds(start_time, DateTime()) < timeout):
            time.sleep(AppiumForIOSUtils.CHECK_WEBKIT_DEBUG_PROXY_STATUS_INTERVAL)
            is_started = AppiumForIOSUtils.is_webkit_debug_proxy_start()

        if(not is_started):
            raise TimeoutException('webkit debug proxy is not started in ' + str(timeout) + ' seconds')

if __name__ == '__main__':
    AppiumForIOSUtils.generate_launch_command()
    #print AppiumUtils.is_appium_start()
