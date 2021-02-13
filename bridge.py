import os
from cache import cache
from flask import current_app
from fredapi import Fred


class Bridge:

    api_key = None

    def __init__(self):
        if 'FRED_API_KEY' in current_app.config:
            self.api_key = current_app.config['FRED_API_KEY']
        else:
            self.api_key = os.environ['FRED_API_KEY']

    @cache.memoize()
    def request(self, data):
        """

        :param data: JSON Object to feed Quandl API request
        :return: JSON object with the response from he API
        """
        current_app.logger.debug("Cache missed")
        try:
            fred = Fred(api_key=self.api_key)
            series = fred.get_series(data.get('series_id'))
            return series.last('1D').get(0)
        except Exception as e:
            raise e

    def __repr__(self):
        return f'{"Bridge()"}'
