import json
import os
from DateTime import DateTime

from axis20.globals import AXIS_UPDATE_AVAILABILITY_API_URL, AXIS_BOOK_PL_BY_TEACHER_API_URL
from axis20.interfaces.etown.datastruct import ClassInfo
from axis20.interfaces.etown.enumeration import ClassServiceType, ClassServiceSubType, MarketCode, LanguageCode, ClassLevel, \
    PartnerCode, \
    EvcServerCode, TimeZone
from axis20.testhelpers.etown.helperbase import axis_schedule_service, super_admin_web_request_session, usvs1_ms_sql
from axis20.testhelpers.etown.student import studenthelper
from axis20.testhelpers.etown.teacher import teacherhelper
from axis20.utilities import filereader

current_dir = os.path.dirname(__file__)
class_info_query = filereader.read(os.path.join(current_dir, "class_info.sql"))

__author__ = 'karl.gong'


def create_class(start_time,
                 center_code,
                 service_type=ClassServiceType.GL,
                 service_sub_type=ClassServiceSubType.Global,
                 class_level=ClassLevel.BEG,
                 language_code=LanguageCode.English,
                 market_code=MarketCode.Global,
                 partner_code=PartnerCode.Global,
                 evc_server_code=EvcServerCode.Adobe_us1):
    """
        Create a class with specified parameters.
    :param start_time: use data struct DateTime
    :param center_code: use enumeration CenterCode
    :param service_type: use enumeration ClassServiceType
    :param service_sub_type: use enumeration ClassServiceSubType
    :param class_level: use enumeration ClassLevel
    :param language_code: use enumeration LanguageCode
    :param market_code: use enumeration MarketCode
    :param partner_code: use enumeration PartnerCode
    :param evc_server_code: use enumeration EvcServerCode
    :return: the information of the created class
    """
    client = axis_schedule_service.client
    create_class_detail = client.factory.create("ns2:CreateClassDetail")
    create_class_detail.ServiceType = service_type
    create_class_detail.ServiceSubType = None if service_sub_type == ClassServiceSubType.Global else service_sub_type
    create_class_detail.StartTime = start_time.toZone(TimeZone.Eastern).asdatetime().strftime("%Y-%m-%dT%H:%M:%S")
    # cp20 is 30 mins and other class type is 60 mins
    class_duration = 1.0 / 48 if service_sub_type == ClassServiceSubType.CP20 else 1.0 / 24
    create_class_detail.EndTime = (start_time + class_duration).toZone(TimeZone.Eastern).asdatetime().strftime(
        "%Y-%m-%dT%H:%M:%S")
    create_class_detail.CenterCode = center_code
    create_class_detail.ClassCount = 1
    create_class_detail.Language = language_code
    create_class_detail.Level = class_level
    create_class_detail.Market = None if market_code == MarketCode.Global else market_code
    create_class_detail.Partner = None if partner_code == PartnerCode.Global else partner_code
    create_class_detail.Unit = None

    array_of_create_class_detail = client.factory.create("ns2:ArrayOfCreateClassDetail")
    array_of_create_class_detail.CreateClassDetail = [create_class_detail]

    create_classes_parameter = client.factory.create("ns2:CreateClassesParameter")
    create_classes_parameter.Classes = array_of_create_class_detail
    create_classes_parameter.StartDate = create_class_detail.StartTime
    create_classes_parameter.EndDate = create_class_detail.EndTime
    create_classes_parameter.EvcServer = evc_server_code

    response = client.service.CreateClasses(create_classes_parameter)

    if response.StatusCode == 0:  # Status code 0 means the class is created successfully.
        class_info = ClassInfo()
        class_info.class_id = response.Classes.UnassignedClassDetail[0].Class_id
        class_info.service_type = service_type
        class_info.service_sub_type = service_sub_type
        class_info.start_time = start_time
        class_info.end_time = start_time + class_duration
        class_info.class_level = class_level
        class_info.language_code = language_code
        class_info.market_code = market_code
        class_info.partner_code = partner_code
        class_info.evc_server_code = evc_server_code
        return class_info
    else:
        raise Exception(
            "Failed to create class, message: [%s], error code: [%s]." % (
                response.Message, response.StatusCode))


def set_availability(member_id, start_time, end_time):
    """
        Set availability for teacher.
    :param member_id: the member of teacher
    :param start_time: set availability for the whole day
    :type start_time: DateTime
    :param end_time: set availability for the whole day
    :type end_time: DateTime
    """
    availability_start_time = start_time.toZone(TimeZone.UTC).asdatetime().strftime("%Y-%m-%dT%H:%M:%SZ")
    availability_end_time = (end_time + 1).toZone(TimeZone.UTC).asdatetime().strftime("%Y-%m-%dT%H:%M:%SZ")
    set_availability_json = {"param":
                                 {"TimeRange":
                                      {"StartTime": availability_start_time,
                                       "EndTime": availability_end_time},
                                  "TeacherMemberId": member_id,
                                  "AvailabilityDetail": [{
                                      "TeacherMemberId": member_id,
                                      "StartTime": availability_start_time,
                                      "EndTime": availability_end_time}]
                                  }
                             }
    response = super_admin_web_request_session.post(AXIS_UPDATE_AVAILABILITY_API_URL, json=set_availability_json)
    response_content = json.loads(response.content)

    if response_content[0]["status"] != 0:  # Status 0 means the availability is set successfully.
        raise Exception(
            "Failed to set availability, message: [%s], error code: [%s]." % (
                response_content[0]["id"], response_content[0]["status"]))


def assign_class(class_id, member_id):
    """
        Assign class to teacher.
    :param class_id: the class id
    :param member_id: the member id of teacher
    """
    client = axis_schedule_service.client
    assign_class_parameter = client.factory.create("ns1:AssignClassParameter")
    assign_class_parameter.class_id = class_id
    assign_class_parameter.member_id = member_id
    response = client.service.AssignClass(assign_class_parameter)

    if response.StatusCode != 0:  # Status code 0 means the class is assigned successfully.
        raise Exception(
            "Failed to assign class, message: [%s], error code: [%s]." % (
                response.Message, response.StatusCode))


def delete_class(class_id):
    """
        Delete a future class.
    :param class_id: the class id
    """
    client = axis_schedule_service.client
    array_of_class_ids = client.factory.create("ns9:ArrayOfint")
    array_of_class_ids.int = [class_id]

    delete_class_parameter = client.factory.create("ns2:DeleteClassParameter")
    delete_class_parameter.ClassIds = array_of_class_ids
    delete_class_parameter.OperatorMemberId = -1

    response = client.service.DeleteClass(delete_class_parameter)

    if response.StatusCode != 0:  # Status code 0 means the class is deleted successfully.
        raise Exception(
            "Failed to delete class, message: [%s], error code: [%s]." % (
                response.Message, response.StatusCode))


def create_class_for_teacher(member_id, start_time, service_type=ClassServiceType.GL,
                             service_sub_type=ClassServiceSubType.Global,
                             class_level=ClassLevel.BEG,
                             language_code=LanguageCode.English,
                             market_code=MarketCode.Global,
                             partner_code=PartnerCode.Global,
                             evc_server_code=EvcServerCode.Adobe_us1):
    """
        Create a class and set availability for teacher
    :param member_id: the member id of teacher
    :param start_time: class start time
    :type start_time: DateTime
    :param service_type: use enumeration ClassServiceType
    :param service_sub_type: use enumeration ClassServiceSubType
    :param class_level: use enumeration ClassLevel
    :param language_code: use enumeration LanguageCode
    :param market_code: use enumeration MarketCode
    :param partner_code: use enumeration PartnerCode
    :param evc_server_code: use enumeration EvcServerCode
    :return: the information of the created class
    """
    class_info = create_class(start_time=start_time, center_code=teacherhelper.get_teacher_info(member_id).center_code,
                              service_type=service_type, service_sub_type=service_sub_type, class_level=class_level,
                              language_code=language_code, market_code=market_code, partner_code=partner_code,
                              evc_server_code=evc_server_code)
    set_availability(member_id, class_info.start_time, class_info.end_time)
    assign_class(class_info.class_id, member_id)
    return class_info


def teacher_book_allocated_pl(class_id, student_member_id, topic, topic_id,
                              service_sub_type=ClassServiceSubType.Global, is_video_class=False):
    """
        Teacher book allocated pl for student
    :param class_id: id of the allocated class
    :param student_member_id: student member id
    :param topic: selected topic content or custom topic content
    :param topic_id: topic_id for selected topic, 0 for custom topic
    :param service_sub_type: use enumeration ClassServiceSubType
    :param is_video_class: book a video PL or not
    :return: the booked class information
    """
    class_info = get_class_info(class_id)
    booking_start_time = class_info.start_time.toZone(TimeZone.UTC).asdatetime().strftime("%Y-%m-%d %H:%M:%S")
    booking_end_time = class_info.end_time.toZone(TimeZone.UTC).asdatetime().strftime("%Y-%m-%dT%H:%M:%S")
    book_pl_json = {"param":
        {
            "CLassCriteria": {"ClassId": class_id},
            "TeacherCriteria": {
                "TeacherMemberId": class_info.teacher_member_id
            },
            "StudentCriteria": {
                "UserNameOrEmail": studenthelper.get_student_info(student_member_id).user_name
            },
            "Topic": topic,
            "TopicId": topic_id,
            "HasSpecifiedTeacher": False,
            "ServiceSubTypeCode": service_sub_type,
            "StartTime": booking_start_time,
            "EndTime": booking_end_time,
            "IsVideoClass": is_video_class
        }
    }
    response = super_admin_web_request_session.post(AXIS_BOOK_PL_BY_TEACHER_API_URL, json=book_pl_json)
    response_content = json.loads(response.content)

    # Status 0 means the pl booking is successful.
    if response_content[0]["status"] == 0:
        class_info.topic = topic
        class_info.topic_id = topic_id
        return class_info
    else:
        raise Exception(
            "Failed to book allocated PL, message: [%s], error code: [%s]." % (
                response_content[0]["message"], response_content[0]["status"]))


def teacher_book_additional_pl(teacher_member_id, start_time, student_member_id, topic, topic_id,
                               service_sub_type=ClassServiceSubType.Global, is_video_class=False):
    """
        Teacher book additional pl for student
    :param teacher_member_id: teacher member id
    :param start_time: class start time
    :type start_time: DateTime
    :param student_member_id: student member id
    :param topic: selected topic content or custom topic content
    :param topic_id: topic_id for selected topic, 0 for custom topic
    :param service_sub_type: use enumeration ClassServiceSubType
    :param is_video_class: book a video PL or not
    :return:  he booked class informationt
    """
    booking_start_time = start_time.toZone(TimeZone.UTC).asdatetime().strftime("%Y-%m-%d %H:%M:%S")
    # cp20 is 30 minutes and other class type is 60 minutes
    class_duration = 1.0 / 48 if service_sub_type == ClassServiceSubType.CP20 else 1.0 / 24
    booking_end_time = (start_time + class_duration).toZone(TimeZone.UTC).asdatetime().strftime("%Y-%m-%dT%H:%M:%S")
    book_pl_json = {"param":
        {
            "CLassCriteria": None,
            "TeacherCriteria": {
                "TeacherMemberId": teacher_member_id
            },
            "StudentCriteria": {
                "UserNameOrEmail": studenthelper.get_student_info(student_member_id).user_name
            },
            "Topic": topic,
            "TopicId": topic_id,
            "HasSpecifiedTeacher": False,
            "ServiceSubTypeCode": service_sub_type,
            "StartTime": booking_start_time,
            "EndTime": booking_end_time,
            "IsVideoClass": is_video_class
        }
    }
    response = super_admin_web_request_session.post(AXIS_BOOK_PL_BY_TEACHER_API_URL, json=book_pl_json)
    response_content = json.loads(response.content)

    # Status 0 means the pl booking is successful.
    if response_content[0]["status"] == 0:
        class_info = ClassInfo()
        get_class_id_query = """SELECT class_id
                                                FROM Teachers..Class
                                                WHERE TeacherMember_id = {teacher_member_id}
                                                AND StartTime = '{start_time}'"""
        class_info.class_id = usvs1_ms_sql.exec_query_and_fetch_first(get_class_id_query,
                                                                      teacher_member_id=teacher_member_id,
                                                                      start_time=start_time.toZone(TimeZone.Eastern).asdatetime().strftime("%Y-%m-%d %H:%M:%S"))[0]
        class_info.topic = topic
        class_info.topic_id = topic_id
        return class_info
    else:
        raise Exception(
            "Failed to book additional PL, message: [%s], error code: [%s]." % (
                response_content[0]["message"], response_content[0]["status"]))


def student_book_pl(student_member_id, class_id, topic, topic_id,
                    service_sub_type=ClassServiceSubType.Global, is_video_class=False):
    class_info = teacher_book_allocated_pl(class_id, student_member_id, topic, topic_id, service_sub_type,
                                           is_video_class)
    update_student_book_query = """UPDATE Teachers..StudentClassBooking
                                                                SET HasSpecifiedTeacher = 0,
                                                                BookedBy = 'S'
                                                                WHERE Class_id = {class_id}"""
    usvs1_ms_sql.exec_non_query(update_student_book_query, class_id=class_id)
    return class_info


def get_class_info(class_id):
    """
        Get information of  one class by class_id.
    :param class_id: the class id
    :return: the related information of this class
    """
    class_info_tuple = usvs1_ms_sql.exec_query_and_fetch_first(class_info_query, class_id=class_id)
    class_info = ClassInfo()
    class_info.class_id = class_id
    class_info.service_type = class_info_tuple[0]
    class_info.service_sub_type = class_info_tuple[1]
    class_info.start_time = DateTime("%s %s" % (str(class_info_tuple[2]), TimeZone.Eastern))
    class_info.end_time = DateTime("%s %s" % (str(class_info_tuple[3]), TimeZone.Eastern))
    class_info.class_level = class_info_tuple[4]
    class_info.language_code = class_info_tuple[5]
    class_info.market_code = class_info_tuple[6]
    class_info.partner_code = class_info_tuple[7]
    class_info.evc_server_code = class_info_tuple[8]
    class_info.teacher_member_id = class_info_tuple[9]
    return class_info
