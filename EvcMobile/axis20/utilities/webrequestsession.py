import threading
import requests

class WebRequestSession:
    def __init__(self, login_handler_url, username, password):
        self.__login_handler_url = login_handler_url
        self.__username = username
        self.__password = password
        self.__is_logged_in = False
        self.__session = requests.session()
        self.__login_lock = threading.Lock()

    def post(self, url, data=None, json=None, **kwargs):
        self.__login()
        return self.__session.post(url, data=data, json=json, **kwargs)

    def get(self, url, **kwargs):
        self.__login()
        return self.__session.get(url, **kwargs)

    def close(self):
        self.__session.close()

    def __login(self):
        if not self.__is_logged_in:
            self.__login_lock.acquire()
            try:
                if not self.__is_logged_in:
                    self.__session.post(self.__login_handler_url,
                                        data={"username": self.__username, "password": self.__password})
                    self.__is_logged_in = True
            finally:
                self.__login_lock.release()
