import pybithumb

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
        with open("../key.txt", "r") as f:
            self._con_key = f.readline().strip()
            self._sec_key = f.readline().strip()

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