from stockx_wrapper import settings as st
from stockx_wrapper.products.product import Product
from stockx_wrapper.requester import requester


class Products:

    @staticmethod
    def get_product_data(product_id, country='US', currency='USD'):
        """
        Get product data by product id.

        :param product_id: str
        :param country: str, optional
            Country for focusing market information.
        :param currency: str, optional
            Currency to get. Tested with 'USD' and 'EUR'.

        :return: Product
            Product info.
        """

        # Format url and get data
        url = f'{st.API_URL}/{st.GET_PRODUCT}/{product_id}'
        params = {
            'includes': 'market',
            'currency': currency,
            'country': country
        }
        data = requester.get(url=url, params=params)
        _product = data.get('Product')

        if _product:
            return Product(product_data=_product)

        return None

    def search_products(self, product_name, country='US', currency='USD'):
        """
        Search by product name.

        :param product_name: str
        :param country: str, optional
            Country for focusing market information.
        :param currency: str, optional
            Currency to get. Tested with 'USD' and 'EUR'.

        :return: Product
            Product info. First hit.
        """

        # Format url and get data
        url = f'{st.API_URL}/{st.SEARCH_PRODUCTS}'
        params = {
            'page': '1',
            '_search': product_name,
            'dataType': 'product'
        }
        data = requester.get(url=url, params=params)
        products = data.get('Products')

        if products:
            # Return first hit
            product_data = products[0]
            _product = self.get_product_data(product_id=product_data['id'], country=country, currency=currency)
            return _product

        return None

    def search_products_new_api(self, product_name, country='US', currency='USD'):
        """
        Uses new API from Algolia.

        :param product_name: str
        :param country: str, optional
            Country for focusing market information.
        :param currency: str, optional
            Currency to get. Tested with 'USD' and 'EUR'.

        :return: Product
            Product info. First hit.
        """

        body = {
            'query': product_name,
            'facets': '*',
            'filters': ''
        }

        data = requester.post(url=st.ALGOLIA_URL, body=body)
        products = data.get('hits')

        if products:
            # Return first hit
            product_data = products[0]
            _product = self.get_product_data(product_id=product_data['id'], country=country, currency=currency)
            return _product

        return None
