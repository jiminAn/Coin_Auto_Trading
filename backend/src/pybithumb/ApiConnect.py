import pybithumb
import logging

class Connect :
    """
    connect client API
    """
    _con_key = ""
    _sec_key = ""

    def __init__(self):
        """
        initialize connect key & secret key
        """

        with open("./key.txt", "r") as f:
            self.__con_key = f.readline().strip()
            self.__sec_key = f.readline().strip()

        logging.info(f"Login private API with connect key: {self.__con_key}")

    def get_bitumb(self):
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