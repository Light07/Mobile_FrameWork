from DateTime import DateTime

class ClassInfo:

    class_id = None
    topic = ''
    member_id = None # Teacher MemberId.
    start_time = None # yyyy-mm-dd hh:mm:ss DateTime Format
    service_type = None
    service_sub_type = None
    class_level = None # BEG,ELE,INT,UPINT,ADV
    language_code = None
    market_code = None
    partner_code = None
    evc_server_code = None
    category_type = None
    topic_level = None # level 1 ~ level 16
    display_name = None # Teacher Display Name
    status = None # Class Status Name

    def __init__(self, member_id=None, start_time=None, service_type=None, service_sub_type=None,
                 class_level=None, language_code=None, market_code=None, partner_code=None, evc_server_code=None):

        self.member_id = member_id
        self.start_time = start_time
        self.service_type = service_type
        self.service_sub_type = service_sub_type
        self.class_level = class_level
        self.language_code = language_code
        self.market_code = market_code
        self.partner_code = partner_code
        self.evc_server_code = evc_server_code

    def get_class_id(self):
        return self.class_id

    def set_class_id(self, id):
        self.class_id = id

    def get_topic(self):
        return self.topic

    def set_topic(self, topic):
        self.topic = topic

    def get_member_id(self):
        return self.member_id

    def set_member_id(self, member_id):
        self.member_id = member_id

    def get_start_time(self):
        return self.start_time

    def set_start_time(self, start_time):
        self.start_time = start_time

    def set_start_time_by_str(self, start_time, time_zone):
        dt_start_time = DateTime(start_time + ' ' + time_zone)
        self.start_time = dt_start_time

    def get_service_type(self):
        return self.service_type

    def set_service_type(self, service_type):
        self.service_type = service_type

    def get_service_sub_type(self):
        return self.service_sub_type

    def set_service_sub_type(self, service_sub_type):
        self.service_sub_type = service_sub_type

    def get_class_level(self):
        return self.class_level

    def set_class_level(self, class_level):
        self.class_level = class_level

    def get_language_code(self):
        return self.language_code

    def set_language_code(self, language_code):
        self.language_code = language_code

    def get_market_code(self):
        return self.market_code

    def set_market_code(self, market_code):
        self.market_code = market_code

    def get_partner_code(self):
        return self.partner_code

    def set_partner_code(self, partner_code):
        self.partner_code = partner_code

    def get_evc_server_code(self):
        return self.evc_server_code

    def set_evc_server_code(self, evc_server_code):
        self.evc_server_code = evc_server_code

    def get_category_type(self):
        return self.category_type

    def set_category_type(self, category_type):
        self.category_type = category_type

    def get_topic_level(self):
        return self.topic_level

    def set_topic_level(self, topic_level):
        self.topic_level = topic_level

    def get_display_name(self):
        return self.display_name

    def set_display_name(self, display_name):
        self.display_name = display_name

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status

    def clone(self):
        new_class = ClassInfo()
        new_class.set_member_id(self.get_member_id())
        new_class.set_start_time(self.get_start_time())
        new_class.set_class_id(self.get_class_id())
        new_class.set_topic(self.get_topic())
        new_class.set_service_type(self.get_service_type())
        new_class.set_service_sub_type(self.get_service_sub_type())
        new_class.set_class_level(self.get_class_level())
        new_class.set_language_code(self.get_language_code())
        new_class.set_market_code(self.get_market_code())
        new_class.set_partner_code(self.get_partner_code())
        new_class.set_evc_server_code(self.get_evc_server_code())
        new_class.set_category_type(self.get_category_type())
        new_class.set_topic_level(self.get_topic_level())
        new_class.set_display_name(self.get_display_name())
        new_class.set_status(self.get_status())

        return new_class

    def remove_topic_prefix(self, topic):
        if topic.startswith("Unit"):
            return topic.split('-')[1].strip().lower().encode("utf-8")
        else:
            return topic.strip().lower().encode("utf-8")

    def class_equals(self, class_info):
        topic_1 = self.remove_topic_prefix(self.get_topic())
        topic_2 = class_info.remove_topic_prefix(class_info.get_topic())
        display_name_1 = self.get_display_name()
        display_name_2 = class_info.get_display_name()

        # Remove the last '.'
        if display_name_1.endswith('.'):
            display_name_1 = display_name_1[:-1]

        if display_name_2.endswith('.'):
            display_name_2 = display_name_2[:-1]

        return self.get_start_time().equalTo(class_info.get_start_time()) & (topic_1 == topic_2) & (display_name_1 == display_name_2)