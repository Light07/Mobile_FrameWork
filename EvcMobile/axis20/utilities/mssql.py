import pymssql

class MSSQL:

    def __init__(self, host, user, password, db, login_timeout=30, timeout=60, autocommit=True, charset="utf8", appname="ASDAutomation"):
        self.host = host
        self.user = user
        self.password = password
        self.db = db
        self.login_timeout = login_timeout
        self.timeout = timeout
        self.autocommit = autocommit
        self.charset = charset
        self.appname = appname

    def __get_connection(self):
        connect = pymssql.connect(host=self.host, user=self.user, password=self.password, database=self.db,
                                    login_timeout=self.login_timeout, timeout=self.timeout, charset=self.charset, appname=self.appname)
        connect.autocommit(self.autocommit)
        return connect

    def exec_query(self, query, **query_kwargs):
        """
            Execute the query and fetch all the results.
        :param query: the query string
        :param query_kwargs: the format parameters for the query
        :return: all the results
        """
        with self.__get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query.format(**query_kwargs))
            return cursor.fetchall()

    def exec_query_and_fetch_first(self, query, **query_kwargs):
        """
            Execute the query and fetch the first result.
        :param query: the query string
        :param query_kwargs: the format parameters for the query
        :return: the first result
        """
        with self.__get_connection() as connection:
            cursor = connection.cursor()
            cursor.execute(query.format(**query_kwargs))
            return cursor.fetchone()

    def exec_non_query(self, query, **query_kwargs):
        """
            Execute the non query.
        :param query: the query string
        :param query_kwargs: the format parameters for the query
        """
        if self.autocommit:
            with self.__get_connection() as connection:
                cursor = connection.cursor()
                cursor.execute(query.format(**query_kwargs))
        else:
            with self.__get_connection() as connection:
                try:
                    cursor = connection.cursor()
                    cursor.execute(query.format(**query_kwargs))
                    connection.commit()
                except:
                    connection.rollback()
                    raise