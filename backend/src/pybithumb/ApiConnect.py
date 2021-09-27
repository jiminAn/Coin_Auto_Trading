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
        self._sec_key = ""
        self._con_key = ""
        # with open('src/key.txt', "r") as f:
        #     self._con_key = f.readline().strip()
        #     self._sec_key = f.readline().strip()

        # if not self.is_api_key_valid():
        #     logging.error("Key is not valid")
        #     raise ConnectionError
        # else:
        #     logging.info(f"Login private API successfully")

    def log_in(self, con_key, sec_key):
        self._con_key = con_key
        self._sec_key = sec_key

    def get_bithumb(self):
        """
        initialize client Bithumb instance
        :return: Bithumb instance
        """
        return pybithumb.Bithumb(self._con_key, self._sec_key)

    def get_con_key(self):
        """
        get connect key for API
        :return: con_key (String)
        """
        return self._con_key

    def is_api_key_valid(self):
        """
        bithumb api에서 따로 validation 함수를 제공하지 않음
        balance data를 요청하고 이에 대한 에러 코드를 확인하여 validation을 함
        """

        recv_data = pybithumb.Bithumb(self._con_key, self._sec_key).get_balance("BTC")

        if not isinstance(recv_data, tuple):
            if recv_data["message"] == "Invalid Apikey":
                return False
        return True