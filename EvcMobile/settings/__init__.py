#encoding:utf-8

import os

from axis20.interfaces.etown.enumeration import TimeZone
from common.property_utils import PropertyUtils
from common.file_utils import FileUtils
from settings.environment import ENVIRONMENT, UAT_Account, QA_Account, STG_Account

property_utils = PropertyUtils(FileUtils.get_current_file_path(__file__) + os.path.sep + "temp.conf")
Environment = property_utils.get_property_value("ENV")

if Environment == '':
    Environment = ENVIRONMENT.UAT

Environment = ENVIRONMENT.UAT

# initialize user account
if Environment == ENVIRONMENT.UAT:
    WEB_ROOT ="https://uat-evc.ef.com.cn/evc15/meeting/tools/demo"
    Account = UAT_Account
elif Environment == ENVIRONMENT.QA:
    WEB_ROOT ="https://qa-evc.ef.com.cn/evc15/meeting/tools/demo"
    Account = QA_Account
elif Environment == ENVIRONMENT.STAGING:
    Account = STG_Account
    WEB_ROOT ="https://evc.ef.com.cn/evc15/meeting/tools/demo"

# setting for evc15
DB_SLEEP_TIME = 5
DB_TIMEOUT = 120
DEFAULT_SLEEP_TIME = 1
FIND_ELEMENT_TIMEOUT = 60
SEARCH_TIMEOUT = 5
SEARCH_POLL_TIME = 1
LOOP_COUNT = 5
DEFAULT_SLEEP_TIME_FOR_SILVERPOP = 6
LOOP_COUNT_FOR_SILVERPOP = 1200
SALESFORCE_TIMEOUT = 600

# set Test Case Timeout as 3 hours
TESTCASE_TIMEOUT = 600

TIMEOUT = 60

WAIT_FOR_TEXT_TIMEOUT = 30

IMPLICITLY_WAIT_TIME = 120

WAIT_FOR_PAGE_LOAD_TIME = 120

ENTER_CLASS_DELAY_MINUTES = 10

MINUTES_IN_ONE_DAY = 60 * 24

WAIT_PAGE_REFRESH = 5

URL_CHECK_INTERVAL = 5

# control find text timeout
GET_ELEMENT_TEXT_TIMEOUT = 10

TIMEOUT_FOR_ACTIVE = 300

SLEEP_INTERVAL = 1

# control the wait for enter class button timeout - minutes
WAIT_FOR_ENTER_CLASS_BUTTON_TIMEOUT = 10

# control re_run function, default is True
RE_RUN_FLAG = False

# if debug tests cases locally then keep the browser active after execution done. Default value is False
DEBUG_RUN = False

# set queue_size as 10 means that there are at most 10 tests cases can be executed concurrently
QUEUE_SIZE = 1

SEARCH_POLL_TIME = 1

FIREFOX_BINARY = None
FIREFOX_PROFILE = None

SERVER_TIME_ZONE = TimeZone.Eastern
LOCAL_TIME_ZONE = TimeZone.China
TIME_FORMAT_ON_TIME_SLOT = "%Y%m%d %H:%M:%S"
TIME_FORMAT_FOR_SCHEDULE_CLASS = "%Y-%m-%d %H:%M:%S"


IOS_DEVICE_NAME = "Jenkins's iPhone"
ANDROID_DEVICE_NAME = "Redmi"
APPIUM_SERVER_IP = '127.0.0.1'
APPIUM_SERVER_PORT = '4723'
COMMAND_TIMEOUT = '7200'
APP_NAME = 'evc.apk'
ANDROID_APPIUM_PROCESS = "node.exe"
ANDROID_NODE_PATH = r"C:\Program Files (x86)\Appium\node.exe"
ANDROID_APPIUM_PATH = r"C:\Program Files (x86)\Appium\node_modules\appium\bin\appium.js"

# Teacher Name
TEACHER_NAME_1 = 'Teacher1'
TEACHER_NAME_2 = 'Teacher2'
TEACHER_NAME_3 = 'Teacher3'
TEACHER_NAME_4 = 'Teacher4'

# Student Name
STUDENT_NAME_1 = 'Student1'
STUDENT_NAME_2 = 'Student2'
STUDENT_NAME_3 = 'Student3'
STUDENT_NAME_4 = 'Student4'
