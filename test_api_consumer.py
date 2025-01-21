import pytest
import requests
from api_consumer import APIConsumer

class TestAPIConsumer:
    @pytest.fixture
    def api_consumer(self):
        return APIConsumer("http://example.com/api")
        
    def test_make_request_success(self, api_consumer, mocker):
        mock_get = mocker.patch('requests.Session.request')
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"key": "value"}
        
        response = api_consumer._make_request("GET", "/test")
        assert response == {"key": "value"}
        
    def test_make_request_failure(self, api_consumer, mocker):
        mock_get = mocker.patch('requests.Session.request')
        mock_get.return_value.status_code = 500
        mock_get.return_value.raise_for_status.side_effect = requests.exceptions.HTTPError()
        
        response = api_consumer._make_request("GET", "/test")
        assert response is None