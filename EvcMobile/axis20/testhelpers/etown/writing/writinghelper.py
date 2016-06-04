import os

from axis20.interfaces.etown.datastruct import WritingInfo
from axis20.interfaces.etown.enumeration import DataStore
from axis20.testhelpers.etown.helperbase import usvs1_ms_sql, cnvs1_ms_sql, axis_us_writing_service, axis_cn_writing_service
from axis20.testhelpers.etown.school import schoolhelper
from axis20.testhelpers.etown.student import studenthelper
from axis20.utilities import filereader



current_dir = os.path.dirname(__file__)
writing_info_query = filereader.read(os.path.join(current_dir, "writing_info.sql"))


def submit_writing(student_member_id, student_course_id, activity_id, content):
    """
        Simulate a student to submit a writing.
    :param student_member_id: the student member id
    :param student_course_id: the student course id
    :param activity_id: the activity id of the writing
    :param content: the content of the writing
    :return: the information of the submitted writing
    """
    student_info = studenthelper.get_student_info(student_member_id)
    activity_info = schoolhelper.get_activity_info(activity_id)
    if student_info.data_store == DataStore.US:
        client = axis_us_writing_service.client
    else:
        client = axis_cn_writing_service.client
    new_writing_param = client.factory.create("ns1:NewWritingParam")
    new_writing_param.Activity_id = activity_id
    new_writing_param.ContentText = content
    new_writing_param.LanuageCode = "en"
    new_writing_param.LevelCode = schoolhelper.to_level_code(activity_info.standard_level_code)
    new_writing_param.MarketCode = student_info.country
    new_writing_param.PartnerCode = student_info.partner_site
    new_writing_param.StudentCourse_id = student_course_id
    new_writing_param.StudentMember_id = student_member_id
    new_writing_param.Topic = activity_info.topic_blurb
    new_writing_param.WritingTypeCode = schoolhelper.to_writing_type_code(activity_info.grade_mode)
    new_writing_param.CourseName = activity_info.course_name
    new_writing_param.LevelName = schoolhelper.to_level_name(activity_info.level_no, activity_info.unit_no)
    response = client.service.SubmitWriting(new_writing_param)
    if response.StatusCode == 0:  # Status code 0 means the writing is submitted successfully.
        writing_info = WritingInfo()
        writing_info.data_store = student_info.data_store
        writing_info.writing_id = response.Writing_id
        writing_info.activity_id = new_writing_param.Activity_id
        writing_info.content = new_writing_param.ContentText
        writing_info.language_code = new_writing_param.LanuageCode
        writing_info.level_code = new_writing_param.LevelCode
        writing_info.market_code = new_writing_param.MarketCode
        writing_info.partner_code = new_writing_param.PartnerCode
        writing_info.student_course_id = new_writing_param.StudentCourse_id
        writing_info.student_member_id = new_writing_param.StudentMember_id
        writing_info.topic_blurb = new_writing_param.Topic
        writing_info.writing_type_code = new_writing_param.WritingTypeCode
        writing_info.course_name = new_writing_param.CourseName
        writing_info.level_name = new_writing_param.LevelName
        return writing_info
    else:
        raise Exception(
            "Failed to submit writing, message: [%s], error code: [%s]." % (response.Message, response.StatusCode))


def allocate_writing_to_center(data_store, writing_id, center, skill_group_id):
    """
        Simulate allocating a writing to a center.
    :param data_store: use enumeration DataStore
    :param writing_id: the writing id
    :param center: use enumeration Center
    :param skill_group_id: the skill group id of the writing
    """
    if data_store == DataStore.US:
        vs1_ms_sql = usvs1_ms_sql
    else:
        vs1_ms_sql = cnvs1_ms_sql
    query = """
    INSERT INTO AcademicContent..WritingQueue
    (Writing_id, OriginalCenterCode, StatusCode, CorrectionTypeCode, SkillGroup_id)
    VALUES({writing_id}, '{center}', 'Allocated', 'Teacher', {skill_group_id})
    """
    vs1_ms_sql.exec_non_query(query, writing_id=writing_id, center=center, skill_group_id=skill_group_id)


def get_writing_info(data_store, writing_id):
    """
        Get the information of the writing.
    :param data_store: use enumeration DataStore
    :param writing_id: the writing id
    :return: the information of the writing
    """
    if data_store == DataStore.US:
        vs1_ms_sql = usvs1_ms_sql
    else:
        vs1_ms_sql = cnvs1_ms_sql
    writing_info_tuple = vs1_ms_sql.exec_query_and_fetch_first(writing_info_query, writing_id=writing_id)
    writing_info = WritingInfo()
    writing_info.data_store = data_store
    writing_info.writing_id = writing_info_tuple[0]
    writing_info.activity_id = writing_info_tuple[1]
    writing_info.content = writing_info_tuple[2]
    writing_info.language_code = writing_info_tuple[3]
    writing_info.level_code = writing_info_tuple[4]
    writing_info.market_code = writing_info_tuple[5]
    writing_info.partner_code = writing_info_tuple[6]
    writing_info.student_course_id = writing_info_tuple[7]
    writing_info.student_member_id = writing_info_tuple[8]
    writing_info.topic_blurb = writing_info_tuple[9]
    writing_info.writing_type_code = writing_info_tuple[10]
    writing_info.course_name = writing_info_tuple[11]
    writing_info.level_name = writing_info_tuple[12]
    writing_info.corrector_member_id = writing_info_tuple[13]
    writing_info.grade_template_code = writing_info_tuple[14]
    writing_info.grade_score = writing_info_tuple[15]
    writing_info.comment = writing_info_tuple[16]
    return writing_info
