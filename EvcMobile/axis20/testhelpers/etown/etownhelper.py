import re

from ptest import config
from ptest.plogger import pconsole
import memcache

from axis20.globals import ETOWN_MEMCACHED_SERVER, \
    ETOWN_URL, AXIS_CLAIM_WRITING_PAGE_URL, ETOWN_LOGIN_HANDLER_URL
from axis20.framework.waits.timeoutexception import TimeoutException
from axis20.framework.waits.waiter import Waiter
from axis20.testhelpers.etown.helperbase import usvs1_ms_sql
from axis20.utilities.webrequestsession import WebRequestSession



ETOWN_WARM_UP_USERNAME = config.get_property("etown.warm.up.username")
ETOWN_WARM_UP_PASSWORD = config.get_property("etown.warm.up.password")
ETOWN_WARM_UP_TIMEOUT = config.get_int_property("etown.warm.up.timeout")


def warm_up_etown(username=ETOWN_WARM_UP_USERNAME, password=ETOWN_WARM_UP_PASSWORD, timeout=ETOWN_WARM_UP_TIMEOUT):
    pconsole.write_line("[%s] Warning up ETown." % __name__)
    try:
        Waiter.wait_for(is_etown_warm, timeout=timeout, username=username, password=password)
    except TimeoutException as toe:
        pconsole.write_line("[%s] %s" % (__name__, toe.message))


def is_etown_warm(username, password):
    try:
        session = WebRequestSession(ETOWN_LOGIN_HANDLER_URL, username, password)
        session.get(AXIS_CLAIM_WRITING_PAGE_URL)
        # This is just for warming up, so hard code here.
        session.get(
            ETOWN_URL + "/axismini/miniwriting/getwritinglevelname?studentCourse_id=94804621&activity_id=128695")
        return True
    except Exception:
        return False


def get_localized_text(blurb_text):
    """
        Get the localized text.
        Note: Currently this function only provides the localized text for English.
    :param blurb_text: the blurb text like"getTrans::12345" in the database
    :return: the localized text
    """

    def get_translation(text_resource_id):
        query = "SELECT DefaultText from axis20.WebContent..TextResource WHERE TextResource_Id = {text_resource_id}"
        return usvs1_ms_sql.exec_query_and_fetch_first(query, text_resource_id=text_resource_id)[0]

    return re.sub(r"getTrans::(\d+)", lambda match: get_translation(match.group(1)), blurb_text)


def clear_memcached(key):
    """
        Clear the memcached.
    :param key: the memcached key
    """
    mc = memcache.Client([ETOWN_MEMCACHED_SERVER])
    mc.delete(key)


def clear_writing_datastore_memcached(center, skill_groups):
    """
        Clear the writing datastore memcached.
    :param center: use enumeration Center
    :param skill_groups: the skill groups, this parameter should be a list or tuple
    """
    key = "et_teachertools_writing_datastore_" + center \
          + "_" + ",".join([str(skill_group) for skill_group in sorted(skill_groups)])
    clear_memcached(key)
