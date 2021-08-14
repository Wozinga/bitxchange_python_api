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

    delete = get
    put = get
    post = get

class FakeSessionJSONFailed:
    def get(*args, **kwargs):
        return ResponseJSONFailing()

    delete = get
    put = get
    post = get

class FakeSessionJSONEmptyFailed:
    def get(*args, **kwargs):
        return ResponseJSONEmptyFailing()

    delete = get
    put = get
    post = get


class TestAPI:

    api = API(key="key", secret="secret", base_url="https://test.com")

    method_object_map = [
        ("GET", api.session.get),
        ("Get", api.session.get),
        ("get", api.session.get),
        ("POST", api.session.post),
        ("Post", api.session.post),
        ("post", api.session.post),
        ("DELETE", api.session.delete),
        ("Delete", api.session.delete),
        ("delete", api.session.delete)
    ]

    def test_send_request_json_success(self):

        api = API(key="key", secret="secret", base_url="https://test.com")
        api.session = FakeSession()
        resp = api.send_request("GET", "/some/path")
        
        assert resp == {"output": 10}

    def test_send_request_json_failing(self):

        api = API(key="key", secret="secret", base_url="https://test.com")
        api.session = FakeSessionJSONFailed()
        resp = api.send_request("GET", "/some/path")
        
        assert resp == {"data": "some data"}

    def test_send_request_json_empty_failing(self):

        api = API(key="key", secret="secret", base_url="https://test.com")
        api.session = FakeSessionJSONEmptyFailed()


        with pytest.raises(ValueError, match="Response from backend is empty!"):
            api.send_request("GET", "/some/path")
    
    @pytest.mark.parametrize('method_name, session_func', method_object_map)
    def test_dispatch_request_success(self, method_name, session_func):

        assert self.api._dispatch_request(method_name) == session_func
 

    def test_dispatch_request_get_failing(self):

        http_method = "PUT"
        with pytest.raises(ValueError, match=f"{http_method} not supported!"):
            self.api._dispatch_request(http_method)
            
            
    