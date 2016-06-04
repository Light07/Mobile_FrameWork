import os

from axis20.interfaces.etown.datastruct import ActivityInfo
from axis20.utilities import filereader
from axis20.testhelpers.etown.helperbase import usvs1_ms_sql



current_dir = os.path.dirname(__file__)
activity_info_query = filereader.read(os.path.join(current_dir, "activity_info.sql"))


def get_activity_info(activity_id):
    """
        Get information of the activity.
    :param activity_id: the activity id
    :return: the information of the activity
    """
    activity_info_tuple = usvs1_ms_sql.exec_query_and_fetch_first(activity_info_query, activity_id=activity_id)
    activity_info = ActivityInfo()
    activity_info.course_name = activity_info_tuple[0]
    activity_info.topic_blurb = activity_info_tuple[1]
    activity_info.standard_level_code = activity_info_tuple[2]
    activity_info.level_no = activity_info_tuple[3]
    activity_info.unit_no = activity_info_tuple[4]
    activity_info.grade_mode = activity_info_tuple[5]
    return activity_info


def to_level_name(level_no, unit_no):
    """
        Convert the level number and unit number to Axis level name.
    :param level_no:  the level number
    :param unit_no:  the unit number
    :return: the level name in Axis
    """
    return "Level %s - Unit %s" % (level_no, unit_no)


def to_level_code(standard_level_code):
    """
        Convert the standard level code to Axis level code.
    :param standard_level_code: the standard level code
    :return: the level code in Axis
    """

    def to_int(level_code):
        if level_code == "0A":
            return -1
        elif level_code == "0B":
            return 0
        else:
            return int(level_code)

    query = """
        SELECT LevelCode,MinStandardLevelCode,MaxStandardLevelCode
        from axis20.SchoolPlatform..LevelMap
        WHERE appcode='axisstage'
        """
    level_map = usvs1_ms_sql.exec_query(query)
    for level_info in level_map:
        if to_int(level_info[1]) <= to_int(standard_level_code) <= to_int(level_info[2]):
            return level_info[0]
    raise Exception("Cannot convert standard level code [%s] to level code." % standard_level_code)


def to_writing_type_code(grade_mode):
    """
        Convert the grade mode to Axis writing type code.
    :param grade_mode: the grade mode
    :return: the writing type code in Axis
    """
    if grade_mode == 1:
        return "NoGrade"
    elif 2 <= grade_mode <= 4:
        return "Normal"
    raise Exception("Cannot covert grade mode [%s] to writing type code." % grade_mode)
