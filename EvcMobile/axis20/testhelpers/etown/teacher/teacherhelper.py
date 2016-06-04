import os
from axis20.interfaces.etown.datastruct import TeacherInfo
from axis20.testhelpers.etown.helperbase import usvs1_ms_sql
from axis20.utilities import filereader

current_dir = os.path.dirname(__file__)
teacher_info_query = filereader.read(os.path.join(current_dir, "teacher_info.sql"))


def get_teacher_info(member_id):
    """
        Get information of the teacher.
    :param member_id: the teacher member id
    :return: the information of the teacher
    """
    teacher_info_tuple = usvs1_ms_sql.exec_query_and_fetch_first(teacher_info_query, member_id=member_id)
    teacher_info = TeacherInfo()
    teacher_info.member_id = member_id
    teacher_info.user_name = teacher_info_tuple[0]
    teacher_info.password = teacher_info_tuple[1]
    teacher_info.center_code = teacher_info_tuple[2]
    return teacher_info
