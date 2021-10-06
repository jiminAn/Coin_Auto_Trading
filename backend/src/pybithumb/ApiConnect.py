import pybithumb
import logging
import os

"""
pybithumb.Bithumb 함수들
https://github.com/sharebook-kr/pybithumb/blob/master/pybithumb/client.py
"""


# 수정해야됨
class Connect:
    """
    connect client API
    """

    def __init__(self):
        '''
        intialize secrete key and connect key to empty string
        '''
        self._sec_key = ""
        self._con_key = ""

    def log_in(self, con_key, sec_key):
        '''
        Log in with client's connect key and secrete key
        :param con_key: connect key(Str)
        :parma sec_key: secrete key(Str)
        '''
        self._con_key = con_key
        self._sec_key = sec_key

    def get_bithumb(self):
        '''
        initialize client Bithumb instance
        :return: Bithumb instance
        '''
        return pybithumb.Bithumb(self._con_key, self._sec_key)

    def get_con_key(self):
        '''
        get connect key for API
        :return: con_key (String)
        '''
        return self._con_key

    def is_api_key_valid(self):
        '''
        validate the api key
        :return: Invalid APIkey(False)/ valud APIkey(True)
        '''

        recv_data = pybithumb.Bithumb(self._con_key, self._sec_key).get_balance("BTC")

        if not isinstance(recv_data, tuple):
            if recv_data["message"] == "Invalid Apikey":
                return False
        return True
