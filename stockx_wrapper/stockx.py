from stockx_wrapper.products import Products
from stockx_wrapper.requester import Requester


class Stockx:

    def __init__(self):

        self.requester = Requester()
        self.products = Products(requester=self.requester)
