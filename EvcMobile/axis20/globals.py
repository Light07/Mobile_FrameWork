from ptest import config
from settings import property_utils

__author__ = 'karl.gong'

UAT = "uat"
QA = "qa"

current_env = property_utils.get_property_value("ENV")
if current_env == "apollouat":
    current_env = "uat"

# ETown
ETOWN_MEMCACHED_SERVER = {
    UAT: "10.128.34.195:11211",
    QA: ""
}[current_env]

ETOWN_URL = {
    UAT: "http://lolita.englishtown.com",
    QA: "http://qa.englishtown.com"
}[current_env]

ETOWN_CN_URL = {
    UAT: "http://devcn.englishtown.com",
    QA: "http://qacn.englishtown.com"
}[current_env]

ETOWN_LOGIN_PAGE_URL = ETOWN_URL + "/axis/login?returnurl=%2f"

ETOWN_LOGIN_HANDLER_URL = ETOWN_URL + "/login/handler.ashx"

ETOWN_SUPER_ADMIN_USERNAME = {
    UAT: "kgong",
    QA: "freshmeat"
}[current_env]

ETOWN_SUPER_ADMIN_PASSWORD = {
    UAT: "1",
    QA: "1"
}[current_env]

# Axis
AXIS_CLAIM_WRITING_PAGE_URL = ETOWN_URL + "/axis/writing/index"

AXIS_TEACHER_SCHEDULE_PAGE_URL = ETOWN_URL + "/axis/2/class/teacherschedule"

# ETown database server us vs1
ETOWN_DBSERVER_US_VS1_HOST = {
    UAT: "cns-etdbdevvs1",
    QA: "USB-ETOWNQADB"
}[current_env]

ETOWN_DBSERVER_US_VS1_USERNAME = {
    UAT: "TestUser",
    QA: "TestUser"
}[current_env]

ETOWN_DBSERVER_US_VS1_PASSWORD = {
    UAT: "testuserdev",
    QA: "testuserqa"
}[current_env]

ETOWN_DBSERVER_US_VS1_DB = "ET_Main"

# ETOWN database server cn vs1
ETOWN_DBSERVER_CN_VS1_HOST = {
    UAT: "cns-etdbdevcn1",
    QA: ""
}[current_env]

ETOWN_DBSERVER_CN_VS1_USERNAME = {
    UAT: "TestUser",
    QA: ""
}[current_env]

ETOWN_DBSERVER_CN_VS1_PASSWORD = {
    UAT: "testuserdev",
    QA: ""
}[current_env]

ETOWN_DBSERVER_CN_VS1_DB = "ET_Main"

# Web Service
AXIS_US_WRITING_SERVICE_URL = ETOWN_URL + "/axissatellite/1.0/WritingService.svc?wsdl"
AXIS_CN_WRITING_SERVICE_URL = ETOWN_CN_URL + "/axissatellite/1.0/WritingService.svc?wsdl"

AXIS_SCHEDULE_SERVICE_URL = ETOWN_URL + "/services/axis/1.0/ScheduleService.svc?wsdl"

AXIS_PL_SERVICE_URL = ETOWN_URL + "/services/axis/1.0/StudentPrivateLessonService.svc?wsdl"

# Web API
AXIS_UPDATE_AVAILABILITY_API_URL = ETOWN_URL + "/services/api/axis/command/teachercommand/UpdateAvailability"

AXIS_BOOK_PL_BY_TEACHER_API_URL = ETOWN_URL + "/services/api/axis/command/classcommand/bookplbyteacher"