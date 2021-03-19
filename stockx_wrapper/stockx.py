import json
import requests

from stockx_wrapper import settings as st


class Stockx:

    def __init__(self):

        self.headers = {
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0',
            'sec-fetch-dest': 'none',
            'accept': '*/*',
            'sec-fetch-site': 'cross-site',
            'sec-fetch-mode': 'cors',
            'accept-language': 'en-US'
        }

    def __get(self, url):
        """
        Perform a http get request.

        :param url: str
        :return: dict
            Json format
        """
        response = requests.get(url, headers=self.headers)
        data = json.loads(response.content)
        return data

    def __post(self, url, body):
        """
        Perform a http post request.

        :param url:
        :param body:
        :return:
        """

        response = requests.post(url, headers=self.headers, json=body)
        data = json.loads(response.content)
        return data

    def get_product_data(self, product_id, country='US', currency='USD', output_keys=None):
        """
        Get product data by product id.

        :param product_id: str
        :param country: str, optional
            Country for focusing market information.
        :param currency: str, optional
            Currency to get. Tested with 'USD' and 'EUR'.
        :param output_keys: list, optional
            List of strings. If not empty, return dict will contain just these keys.
        :return: dict
            Json format. Product info.
        """

        # Format url and get data
        url = f'{st.GET_PRODUCT}/{product_id}?includes=market&currency={currency}&country={country}'
        data = self.__get(url)
        product = data.get('Product')

        if not product:
            return None

        if not output_keys:
            return product

        return_data = {}

        for key in output_keys:
            return_data[key] = product.get(key)

        return return_data

    def get_product_specific_size(self, product_id, size):
        """
        Get child product from product id with specified size in US size localization.

        :param product_id: str
        :param size: str
        :return: dict
            Json format. Product info with specified size.
        """

        # get parent product
        parent_product = self.get_product_data(product_id)

        # iterate its children until found one that matches asked size
        for child_id, child_data in parent_product['children'].items():
            if child_data['shoeSize'] == size:
                return child_data

        return None

    def search_products(self, product_name):
        """
        Search by product name.

        :param product_name: str
        :return: dict
            First hit
        """

        # Replace spaces to hexadecimal
        product_name = product_name.replace(' ', '%20')

        # Format url and get data
        url = f'{st.SEARCH_PRODUCTS}?&page=1&_search={product_name}&dataType=product'
        data = self.__get(url)
        products = data.get('Products')

        if products:
            # Return first hit
            return data['Products'][0]

        return None

    def search_products_new_api(self, product_name):
        """
        Uses new API from Algolia.

        :param product_name:
        :return:
        """
        # Replace spaces to hexadecimal
        product_name = product_name.replace(' ', '%20')

        body = {
            'params': f'query={product_name}&facets=*&filters='
        }

        data = self.__post(url=st.ALGOLIA_URL, body=body)
        products = data.get('Products')

        if products:
            # Return first hit
            return data['Products'][0]

        return None
