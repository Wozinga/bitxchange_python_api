import pytest

from requests.models import Response
from bitxchange.api import API

class ResponseJSONPassing:

    def json(*args, **kwargs):
        return {"output": 10}

    @property
    def text(self):
        return "some data"

class ResponseJSONFailing(ResponseJSONPassing):

    def json(*args, **kwargs):
        raise ValueError()

class ResponseJSONEmptyFailing(ResponseJSONPassing):

    def json(*args, **kwargs):
        return {}

class FakeSession:

    def get(*args, **kwargs):
        return ResponseJSONPassing()

    put = get
    post = get

class FakeSessionJSONFailed:
    def get(*args, **kwargs):
        return ResponseJSONFailing()

    put = get
    post = get

class FakeSessionJSONEmptyFailed:
    def get(*args, **kwargs):
        return ResponseJSONEmptyFailing()

    put = get
    post = get


class TestAPI:
    # base_url can be anything as its not being called
    api = API(key="key", secret="secret", base_url="https://test.com")

    method_object_map = [
        ("GET", api.session.get),
        ("Get", api.session.get),
        ("get", api.session.get),
        ("POST", api.session.post),
        ("Post", api.session.post),
        ("post", api.session.post)
    ]

    def test_send_request_json_success(self):
        """
            api.send_request(<http_method>, <url_path>, <data>)
            should return a passing JSON response from exchange.
        """
        # GIVEN I have a valid http_method, url_path and data dict
        # WHEN I send that request to the exchange for processing
        # THEN I am returnd a positive JSON response containing my result

        api = API(key="key", secret="secret", base_url="https://test.com")
        api.session = FakeSession()
        resp = api.send_request("GET", "/some/path")
        
        assert resp == {"output": 10}

    def test_send_request_json_failing(self):
        """
            api.send_request(<http_method>, <url_path>, <data>)
            should return a passing JSON response from exchange.
        """
        # GIVEN I have an http_method, url_path and data dict with violation
        # WHEN I send that request to the exchange for processing and it 
        # THEN I am returnd a failing JSON response containing a complaint

        api = API(key="key", secret="secret", base_url="https://test.com")
        api.session = FakeSessionJSONFailed()
        resp = api.send_request("GET", "/some/path")
        
        assert resp == {"data": "some data"}

    def test_send_request_json_empty_failing(self):
        """
            api.send_request(<http_method>, <url_path>, <data>)
            should return a passing JSON response from exchange.
        """
        # GIVEN I have a valid http_method, url_path and data dict
        # WHEN I send that request to the exchange for processing and a null is returned
        # THEN I am notified that the exchange has returned a null value with an error

        api = API(key="key", secret="secret", base_url="https://test.com")
        api.session = FakeSessionJSONEmptyFailed()

        with pytest.raises(ValueError):
            api.send_request("GET", "/some/path")
    
    @pytest.mark.parametrize('method_name, session_func', method_object_map)
    def test_dispatch_request_success(self, method_name, session_func):
        """
            api._dispatch_request(<http_method>)
            should validate http_method is valid and return session & request
        """
        # GIVEN I have selected a permitted http method
        # WHEN I call the _dispatch request method
        # THEN I returned an active http session of that method type

        assert self.api._dispatch_request(method_name) == session_func
 

    def test_dispatch_request_get_failing(self):
        """
            api._dispatch_request(<http_method>)
            should validate http_method is valid and return session & request
        """
        # GIVEN I have selected a non-permitted http method
        # WHEN I call the _dispatch request method
        # THEN I returned a ValueError warning notifying me of the violation

        http_method = "PUT"
        with pytest.raises(ValueError, match=f"{http_method} not supported!"):
            self.api._dispatch_request(http_method)
            
            
    