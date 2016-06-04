import os

from axis20.interfaces.etown.datastruct import StudentInfo
from axis20.interfaces.etown.enumeration import DataStore
from axis20.testhelpers.etown.helperbase import usvs1_ms_sql, cnvs1_ms_sql
from axis20.utilities import filereader



current_dir = os.path.dirname(__file__)
reactivate_expired_student_query = filereader.read(os.path.join(current_dir, "reactivate_expired_student.sql"))


def reactivate_expired_student(member_id):
    """
        Reactivate the student account if expired.
    :param member_id: the student member id
    """
    if get_student_info(member_id).data_store == DataStore.US:
        vs1_ms_sql = usvs1_ms_sql
    else:
        vs1_ms_sql = cnvs1_ms_sql
    vs1_ms_sql.exec_non_query(reactivate_expired_student_query, member_id=member_id)


def reset_student_and_enroll_course(member_id, ge_group_code):
    """
        Reset the student course records (including writing and writing correction records) and enroll a new course.
    :param member_id: the student member id
    :param ge_group_code: the general english group code, value can be "E10", "E13", "Arabe-E13", "ILS-E13", "Saudi-E10"
    """
    if get_student_info(member_id).data_store == DataStore.US:
        vs1_ms_sql = usvs1_ms_sql
    else:
        vs1_ms_sql = cnvs1_ms_sql
    query = "EXEC School..SchoolAutomationTest_ResetAccount {member_id}, '{ge_group_code}'"
    vs1_ms_sql.exec_non_query(query, member_id=member_id, ge_group_code=ge_group_code)


def get_student_info(member_id):
    """
        Get information of the student.
    :param member_id: the student member id
    :return: the information of the student
    """
    query = """SELECT UserName,FirstName,LastName,Country,Email,Gender,Password,PartnerSite,DataStore
    from axis20.ET_Main.dbo.Members
    WHERE MemberId={member_id} and IsStudent=1"""
    student_info_tuple = usvs1_ms_sql.exec_query_and_fetch_first(query, member_id=member_id)
    student_info = StudentInfo()
    student_info.member_id = member_id
    student_info.user_name = student_info_tuple[0]
    student_info.first_name = student_info_tuple[1]
    student_info.last_name = student_info_tuple[2]
    student_info.country = student_info_tuple[3]
    student_info.email = student_info_tuple[4]
    student_info.gender = student_info_tuple[5]
    student_info.password = student_info_tuple[6]
    student_info.partner_site = student_info_tuple[7]
    student_info.data_store = student_info_tuple[8]
    return student_info
