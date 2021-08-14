import json
import logging
import requests

from .__version__ import __version__
# from bitxchange.spot.market import available_trading_pairs


class API(object):
    """
    Description: Returns a list of all active trading pairs on the exchange
    
    GET /api/available_pairs

    Guide:

    Args:
    
    KWargs:
    """

    def __init__(self, base_url, key=None, secret=None):

        self.base_url = base_url
        self.key = key
        self.secret = secret
        self.session = requests.Session()
        self.session.headers.update(
            {
                "apikey": str(self.key),
                "secretkey": str(self.secret)
            }
        )


    def query_exchange(self, url_path, data=None):
        return self.send_request("GET", url_path, data=data)

    def send_request(self, http_method, url_path, data=None):
        from bitxchange.lib.shared_utils import remove_none_values

        if data is None:
            data = {}
        
        url = self.base_url + url_path

        params = remove_none_values(
            {
                "url": url,
                "data": data
            }
        )
        response = self._dispatch_request(http_method)(**params)

        try:
            response_json = response.json()
        except (ValueError, json.JSONDecodeError):
            return {"data": response.text}

        if response_json:
            return response_json

        raise ValueError("Response from backend is empty!")
        
    def _dispatch_request(self, http_method):
        
        http_method = http_method.upper()

        method_map = {
            "GET": self.session.get,
            "DELETE": self.session.delete,
            "POST": self.session.post,
        }

        if http_method not in method_map:
            raise ValueError(f"{http_method} not supported!")

        return method_map[http_method]
