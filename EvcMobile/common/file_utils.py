import os

class FileUtils(object):

    @staticmethod
    def get_current_file_path(file):
        return os.path.split(os.path.realpath(file))[0]

    @staticmethod
    def read_from_file(path):
        f = open(path, 'r')

        return FileUtils.read_from_stream(f.readlines())

    @staticmethod
    def read_from_stream(stream):
        str_list = []

        for line in stream:
            str_list.append(line)

        return ''.join(str_list)

    @staticmethod
    def get_apps_path():
        return os.path.dirname(FileUtils.get_current_file_path(__file__)) + os.path.sep + "apps"

    @staticmethod
    def get_appium_log_file_path_for_ios():
        return FileUtils.get_current_file_path(__file__) + os.path.sep + '..' + os.path.sep + 'log' + os.path.sep + 'ios_appium_log'

    @staticmethod
    def get_appium_log_file_path_for_android():
        return os.path.dirname(FileUtils.get_current_file_path(__file__)) + os.path.sep + 'log' + os.path.sep + 'android_appium_log'

if __name__ == '__main__':
    print FileUtils.get_current_file_path(__file__)
    print FileUtils.read_from_file(FileUtils.get_current_file_path(__file__) + os.path.sep + 'start_appium_for_ios.sh')
    print FileUtils.get_apps_path()
    print FileUtils.get_appium_log_file_path_for_ios()
