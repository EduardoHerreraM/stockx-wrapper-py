import datetime

from stockx_wrapper import settings as st
from stockx_wrapper.requester import Requester


class Prices:

    def __init__(self, requester):
        self.requester = requester

    def get_product_price_data(self, product_id, start_date='all', end_date=datetime.date.today().strftime('%Y-%m-%d'),
                               intervals=100, country='US', currency='USD'):
        """
        Get product price chart. Average price over time.

        :param product_id: str
        :param start_date: str, optional
            Has to be 'all' or 'YYYY-mm-dd' format.
        :param end_date: str, optional
            Has to be 'YYYY-mm-dd' format.
        :param intervals: str, optional
            Number of rows to get. Time between data returned decreases as this param increases.
        :param country: str, optional
            Country for focusing market information.
        :param currency: str, optional
            Currency to get. Tested with 'USD' and 'EUR'.

        :return: list of dicts

        """

        url = f'{st.GET_PRODUCT}/{product_id}/chart'
        params = {
            'start_date': start_date,
            'end_date': end_date,
            'intervals': intervals,
            'currency': currency,
            'country': country
        }
        data = self.requester.get(url=url, params=params)

        if not data:
            return None

        return_data = []

        for price, date_interval in zip(data['series'][0]['data'], data['xAxis']['categories']):
            return_data.append({
                'avgPrice': price,
                'dateInterval': date_interval
            })

        return return_data