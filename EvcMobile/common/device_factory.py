#encoding:utf-8
from entity.device import Device


class DeviceFactory:

    @staticmethod
    def get_device_by_name(device_name):

        device = None

        # Real devices
        if device_name == '张文的 iPhone':
            device = Device(
                device_name,
                'iphone5s',
                'iOS',
                '9.2',
                'fc0e17acfb4b0f6636eeb8a4e3f7f61b440df681'
            )

        # if device_name == "Jenkins's iPhone":
        #     device = Device(
        #         device_name,
        #         'iphone6',
        #         'iOS',
        #         '9.0.2',
        #         'bc22fdf481915073a83ae9dfd833383bf5fc1fb9'
        #     )

        if device_name == "Jenkins's iPhone":
            device = Device(
            device_name,
            'iphone6s',
            'iOS',
            '9.0.2',
            '443555aab18655718f22dbcaa0e58b48206be1fe'
            )

        if device_name == "Light the future":
            device = Device(
                device_name,
                'iphone5s',
                'iOS',
                '9.1',
                '71d699093b82e82a1dc29e9aec25e4a95d0edd24'
            )

        if device_name == "Carina大人":
            device = Device(
                device_name,
                'iPhone 6 Plus',
                'iOS',
                '8.2',
                '7937a23b0ee3912195bb4db0c902aaa3eb1e5c05'
            )

        # Android Real devices
        if device_name == 'Redmi':
            device = Device(
                device_name,
                'Redmi Note 2',
                'Android',
                '5.0',
                ''
            )

        # Simulators
        # Leave udid empty for simulators
        if device_name == 'iPhone 6':
            device = Device(
                device_name,
                'iphone6',
                'iOS',
                '9.3',
                ''
            )

        # Android Simulators
        if device_name == 'Galaxy_6':
            device = Device(
                device_name,
                'Galaxy_6',
                'Android',
                '5.0',
                ''
            )

        return device
