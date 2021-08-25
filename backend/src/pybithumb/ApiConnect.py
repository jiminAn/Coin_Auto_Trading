import pybithumb
import logging

"""
pybithumb.Bithumb 함수들

https://github.com/sharebook-kr/pybithumb/blob/master/pybithumb/client.py
"""

<<<<<<< HEAD
=======
# 수정해야됨
>>>>>>> test-websocket
class Connect(pybithumb.Bithumb) :
    """
    connect client API
    """
    _con_key = ""
    _sec_key = ""

    def __init__(self):
        """
        initialize connect key & secret key
        """
<<<<<<< HEAD

        with open("./key.txt", "r") as f:
            self.__con_key = f.readline().strip()
            self.__sec_key = f.readline().strip()

        if not self.is_api_key_valid():
            logging.error("Key is not valid")
            raise ConnectionError
        else:
            logging.info(f"Login private API successfully")

        super().__init__(self.__con_key, self.__sec_key)
=======
>>>>>>> test-websocket

        with open("./src/pybithumb/key.txt", "r") as f:
            self.__con_key = f.readline().strip()
            self.__sec_key = f.readline().strip()

        if not self.is_api_key_valid():
            logging.error("Key is not valid")
            raise ConnectionError
        else:
            logging.info(f"Login private API successfully")

        super().__init__(self.__con_key, self.__sec_key)

    def get_bithumb(self):
        """
        initialize client Bithumb instance
        :return: Bithumb instance
        """
        return pybithumb.Bithumb(self.__con_key, self.__sec_key)

    def get_con_key(self):
        """
        get connect key for API
        :return: con_key (String)
        """
        return self.__con_key

    def is_api_key_valid(self):
        """
        bithumb api에서 따로 validation 함수를 제공하지 않음
        balance data를 요청하고 이에 대한 에러 코드를 확인하여 validation을 함
        """

        recv_data = pybithumb.Bithumb(self.__con_key, self.__sec_key).get_balance("BTC")
        if not isinstance(recv_data, tuple):
            if recv_data["message"] == "Invalid Apikey":
                return False
        return True