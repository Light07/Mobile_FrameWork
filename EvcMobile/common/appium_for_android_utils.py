import os
import time

from DateTime import DateTime
from selenium.common.exceptions import TimeoutException

import settings
from common import date_time_utils
from common.device_factory import DeviceFactory
from common.file_utils import FileUtils

class AppiumUtils:

    WAIT_FOR_APPIUM_SERVER_STARTUP_TIMEOUT = 10
    WAIT_FOR_APPIUM_SERVER_STOP_TIMEOUT = 5
    DELAY_TIME_FOR_START_CLOSE_APPIUM = 2
    CHECK_APPIUM_STATUS_INTERVAL = 2

    appium_thread = None

    @staticmethod
    def launch_appium():

        AppiumUtils.close_appium()

        AppiumUtils.generate_launch_command()

        command = (FileUtils.get_current_file_path(__file__) + os.path.sep + "start_appium_for_android.bat")

        os.system("%s" % command)

        AppiumUtils.wait_until_appium_start(AppiumUtils.WAIT_FOR_APPIUM_SERVER_STARTUP_TIMEOUT)

    @staticmethod
    def generate_launch_command():
        device = DeviceFactory.get_device_by_name(settings.ANDROID_DEVICE_NAME)

        command_template = FileUtils.read_from_file(FileUtils.get_current_file_path(__file__) + os.path.sep + "start_appium_template_for_android.bat")

        app_absolute_path  = FileUtils.get_apps_path() + os.path.sep + 'evc.apk'
        log_path = FileUtils.get_apps_path() + os.path.sep + ".." + os.path.sep + "log" + os.path.sep + "android_appium_log"

        command = command_template.format(node_exe_path=settings.ANDROID_NODE_PATH, appium_js_path=settings.ANDROID_APPIUM_PATH, server_ip=settings.APPIUM_SERVER_IP, port=settings.APPIUM_SERVER_PORT,
                                          command_timeout=settings.COMMAND_TIMEOUT, platform_version=device.get_platform_version(),
                                          platform_name=device.get_platform_name(), app=app_absolute_path,
                                          device_name=device.get_device_name(), \
                                          log_path =log_path)
        f = open(FileUtils.get_current_file_path(__file__) + os.path.sep + "start_appium_for_android.bat", 'w')
        f.write(command)
        f.close()

    @staticmethod
    def is_appium_start():
        result_stream = os.popen('tasklist|findstr node.exe')
        result = FileUtils.read_from_stream(result_stream.readlines())
        if settings.ANDROID_APPIUM_PROCESS in result:
            return True
        else:
            return False

    @staticmethod
    def wait_until_appium_start(timeout):
        start_time = DateTime()

        is_started = False
        has_log = False
        while (is_started == False or has_log == False) & (date_time_utils.get_diff_in_seconds(start_time, DateTime()) < timeout):
            time.sleep(AppiumUtils.CHECK_APPIUM_STATUS_INTERVAL)
            is_started = AppiumUtils.is_appium_start()
            has_log = AppiumUtils.is_appium_log_file_is_written()

        if(not is_started):
            raise TimeoutException('Appiun server is not started in ' + str(timeout) + ' seconds')

    @staticmethod
    def is_appium_log_file_is_written():
        log = FileUtils.read_from_file(FileUtils.get_appium_log_file_path_for_android())
        if settings.APPIUM_SERVER_IP in log:
            return True
        else:
            return False

    @staticmethod
    def wait_until_appium_stop(timeout):
        start_time = DateTime()

        is_closed = True
        while (is_closed == True) & (date_time_utils.get_diff_in_seconds(start_time, DateTime()) < timeout):
            time.sleep(AppiumUtils.CHECK_APPIUM_STATUS_INTERVAL)
            is_closed = not AppiumUtils.is_appium_start()

        if(not is_closed):
            raise TimeoutException('Appiun server is not stoped in ' + str(timeout) + ' seconds')

    @staticmethod
    def close_appium():
        os.system('taskkill /F /IM node.exe')
        AppiumUtils.wait_until_appium_stop(AppiumUtils.WAIT_FOR_APPIUM_SERVER_STOP_TIMEOUT)

    @staticmethod
    def start_adb():
        os.system('taskkill /F /IM adb.exe')
        os.system('adb devices')

if __name__ == '__main__':
    AppiumUtils.launch_appium()