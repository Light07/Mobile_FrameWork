class Device:

    def get_device_name(self):
        return self.device_name

    def set_device_name(self, device_name):
        self.device_name = device_name

    def get_device_model(self):
        return self.device_model

    def set_device_model(self, device_model):
        self.device_model = device_model

    def get_platform_name(self):
        return self.platform_name

    def set_platform_name(self, platform_name):
        self.platform_name = platform_name

    def get_platform_version(self):
        return self.platform_version

    def set_platform_version(self, platform_version):
        self.platform_version = platform_version

    def get_udid(self):
        return self.udid

    def set_udid(self, udid):
        self.udid = udid

    def __init__(self, device_name, device_model, platform_name, platform_version, udid):
        self.device_name = device_name
        self.device_model = device_model
        self.platform_name = platform_name
        self.platform_version = platform_version
        self.udid = udid
