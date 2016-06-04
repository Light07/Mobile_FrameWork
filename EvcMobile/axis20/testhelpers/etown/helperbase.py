from axis20.globals import ETOWN_DBSERVER_US_VS1_HOST, ETOWN_DBSERVER_US_VS1_USERNAME, ETOWN_DBSERVER_US_VS1_PASSWORD, \
    ETOWN_DBSERVER_US_VS1_DB, ETOWN_DBSERVER_CN_VS1_HOST, ETOWN_DBSERVER_CN_VS1_USERNAME, \
    ETOWN_DBSERVER_CN_VS1_PASSWORD, ETOWN_DBSERVER_CN_VS1_DB, AXIS_US_WRITING_SERVICE_URL, AXIS_CN_WRITING_SERVICE_URL, \
    AXIS_SCHEDULE_SERVICE_URL, ETOWN_SUPER_ADMIN_USERNAME, \
    ETOWN_SUPER_ADMIN_PASSWORD, ETOWN_LOGIN_HANDLER_URL, AXIS_PL_SERVICE_URL
from axis20.utilities import mssql, webservice
from axis20.utilities.webrequestsession import WebRequestSession



usvs1_ms_sql = mssql.MSSQL(ETOWN_DBSERVER_US_VS1_HOST,
                           ETOWN_DBSERVER_US_VS1_USERNAME,
                           ETOWN_DBSERVER_US_VS1_PASSWORD,
                           ETOWN_DBSERVER_US_VS1_DB)
cnvs1_ms_sql = mssql.MSSQL(ETOWN_DBSERVER_CN_VS1_HOST,
                           ETOWN_DBSERVER_CN_VS1_USERNAME,
                           ETOWN_DBSERVER_CN_VS1_PASSWORD,
                           ETOWN_DBSERVER_CN_VS1_DB)

axis_us_writing_service = webservice.WebService(AXIS_US_WRITING_SERVICE_URL)
axis_cn_writing_service = webservice.WebService(AXIS_CN_WRITING_SERVICE_URL)

axis_schedule_service = webservice.WebService(AXIS_SCHEDULE_SERVICE_URL)

axis_pl_service = webservice.WebService(AXIS_PL_SERVICE_URL)

super_admin_web_request_session = WebRequestSession(ETOWN_LOGIN_HANDLER_URL,
                                                    ETOWN_SUPER_ADMIN_USERNAME,
                                                    ETOWN_SUPER_ADMIN_PASSWORD)
