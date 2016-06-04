import threading

from suds.client import Client

class WebService:
    def __init__(self, url):
        self.__url = url
        self.__client = None
        self.__client_lock = threading.Lock()

    @property
    def client(self):
        if self.__client is None:
            self.__client_lock.acquire()
            try:
                if self.__client is None:
                    self.__client = Client(self.__url)
                return self.__client
            finally:
                self.__client_lock.release()
        return self.__client