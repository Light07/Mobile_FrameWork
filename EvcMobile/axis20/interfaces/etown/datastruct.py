"""
This module is created to make the verification for UI data easier.

The structs in this module are the abstractions for UI data and database.
"""
from copy import copy

# all datetime should use DateTime module
from DateTime import DateTime as DateTime


class Week:
    DAYS_OF_A_WEEK = 7

    def __init__(self, week_day):
        """
            Initialize the Week object.
        :param week_day: the DateTime object for one day of the week
        """
        # in DateTime module first day of a week is Sunday
        if week_day.dow() == 0:
            self.monday = week_day - Week.DAYS_OF_A_WEEK + 1
        else:
            self.monday = week_day - week_day.dow() + 1
        self.monday = self.monday.earliestTime()

    def previous_week(self):
        """
            Return the previous week as a new Week object.
        :return: the Week object for previous week
        """
        return Week(self.monday - Week.DAYS_OF_A_WEEK)

    def next_week(self):
        """
            Return the next week as a new Week object.
        :return: the Week object for previous week
        """
        return Week(self.monday + Week.DAYS_OF_A_WEEK)

    def __eq__(self, other):
        return self.monday.Date() == other.monday.Date()

    def __str__(self):
        return "Week [monday: %s, sunday: %s]" % (self.monday.Date(), (self.monday + Week.DAYS_OF_A_WEEK - 1).Date())


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other_point):
        return (self.x, self.y) == (other_point.x, other_point.y)

    def __cmp__(self, other_point):
        if self.x == other_point.x:
            return cmp(self.y, other_point.y)
        return cmp(self.x, other_point.x)

    def __str__(self):
        return "Point: (%s, %s)" % (self.x, self.y)


class PointSet:
    def __init__(self, point_list=None):
        if point_list is None:
            self.point_list = []
        else:
            self.point_list = point_list

    def add(self, point):
        """
            Add a Point into this Point set.

            This has no effect if the element is already present.
        :param point: Point object
        """
        if point not in self.point_list:
            self.point_list.append(point)

    def discard(self, point):
        """
            Discard a point from axis20.this Point Set.

            If the element is not a member, do nothing.
        :param point: Point object
        """
        if point in self.point_list:
            self.point_list.remove(point)

    def union(self, point_set):
        """
            Return the union of Point Sets as a new Point Set.

            (i.e. all elements that are in either set.)
        :param point_set: the other Point Set
        :return: a new Point Set
        """
        new_point_set = PointSet(copy(self.point_list))
        for point in point_set.point_list:
            new_point_set.add(point)
        return new_point_set

    def difference(self, point_set):
        """
            Return the difference of two Point Sets as a new Point Set.

            (i.e. all elements that are in this set but not the other.)
        :param point_set: the other Point Set
        :return: a new Point Set
        """
        new_point_set = PointSet(copy(self.point_list))
        for point in point_set.point_list:
            new_point_set.discard(point)
        return new_point_set

    def __eq__(self, other_point_set):
        return sorted(self.point_list) == sorted(other_point_set.point_list)

    def __str__(self):
        return "PointSet: [%s]" % ", ".join(["(%s, %s)" % (point.x, point.y) for point in self.point_list])


class InfoBase:
    def set_all_attrs_to(self, value):
        """
            Set all attributes in this classes to value.
        :param value: the value to be set
        """
        for key in self.attrs():
            self[key] = value

    def items(self):
        """
            List of this classes's (attr, value) pairs, as 2-tuples.
        """
        return self.__dict__.items()

    def attrs(self):
        """
            List of this classes's attrs.
        """
        return self.__dict__.keys()

    def values(self):
        """
            List of this classes's values.
        """
        return self.__dict__.values()

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, item):
        return getattr(self, item)

    def __eq__(self, other_info):
        """
            Whether this classes equals to other info classes.
            Note:
            1. Attribute with None value is considered as empty string "".
            2. Non-string attribute will be converted to string. e.g., 123 will be converted to "123".
        """
        for key in self.__dict__:
            my_value = "" if self.__dict__[key] is None else str(self.__dict__[key])
            other_value = "" if other_info.__dict__[key] is None else str(other_info.__dict__[key])
            if not my_value == other_value:
                return False
        return True

    def __str__(self):
        return self.__dict__.__str__()

    def __repr__(self):
        return self.__dict__.__repr__()


class ClassInfo(InfoBase):
    def __init__(self):
        self.class_id = None
        self.service_type = None
        self.service_sub_type = None
        self.start_time = None
        self.end_time = None
        self.level = None
        self.language = None
        self.country = None
        self.partner = None
        self.evc_server = None


class WritingInfo(InfoBase):
    def __init__(self):
        self.data_store = None
        self.writing_id = None
        self.activity_id = None
        self.content = None
        self.language_code = None
        self.level_code = None
        self.market_code = None
        self.partner_code = None
        self.student_course_id = None
        self.student_member_id = None
        self.topic_blurb = None
        self.writing_type_code = None
        self.course_name = None
        self.level_name = None
        self.corrector_member_id = None
        self.grade_template_code = None
        self.grade_score = None
        self.comment = None


class StudentInfo(InfoBase):
    def __init__(self):
        self.member_id = None
        self.user_name = None
        self.first_name = None
        self.last_name = None
        self.country = None
        self.email = None
        self.gender = None
        self.password = None
        self.partner_site = None
        self.data_store = None


class TeacherInfo(InfoBase):
    def __init__(self):
        self.member_id = None
        self.user_name = None
        self.password = None
        self.center = None


class ActivityInfo(InfoBase):
    def __init__(self):
        self.course_name = None
        self.topic_blurb = None
        self.standard_level_code = None
        self.level_no = None
        self.unit_no = None
        self.grade_mode = None
