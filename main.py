import requests
import yaml
from openapi_spec_validator import validate_spec
from openapi_spec_validator.readers import read_from_filename
from api_consumer import APIConsumer


def generate_api_consumer(api_spec_url: str) -> None:
    """Generate API consumer class and test file from OpenAPI specification.
    
    Args:
        api_spec_url: URL to the OpenAPI specification file
    """
    try:
        # Download and validate the API specification
        response = requests.get(api_spec_url, headers={'Accept': 'application/json'})
        response.raise_for_status()
        
        print(f"Response status: {response.status_code}")
        print(f"Content-Type: {response.headers.get('Content-Type')}")
        print(f"First 100 chars: {response.text[:100]}")
        
        # Handle potential YAML content
        # Always try YAML first since the content type might not be properly set
        try:
            spec_dict = yaml.safe_load(response.text)
        except yaml.YAMLError:
            # If YAML parsing fails, try JSON
            spec_dict = response.json()
        # Handle potential YAML content
                # Always try YAML first since the content type might not be properly set
        
        # Validate the OpenAPI specification
        validate_spec(spec_dict)
        
        # Generate API consumer class
        with open("api_consumer.py", "w") as f:
            f.write(generate_consumer_code(spec_dict))
            
        # Generate test file
        with open("test_api_consumer.py", "w") as f:
            f.write(generate_test_code(spec_dict))
            
        print("API consumer and test files generated successfully!")       
    except Exception as e:
        print(f"Error generating API consumer: {e}")

def generate_consumer_code(spec_dict: dict) -> str:
    """Generate API consumer class code from OpenAPI specification."""
    code = '''import requests

class APIConsumer:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        
    def _make_request(self, method, endpoint, **kwargs):
        url = f"{self.base_url}{endpoint}"
        try:
            response = self.session.request(method, url, **kwargs)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
'''
    
    # Generate methods for each endpoint
    for path, methods in spec_dict['paths'].items():
        for method, details in methods.items():
            operation_id = details.get('operationId', '').replace('-', '_')
            if operation_id:
                code += f'''
    def {operation_id}(self, **kwargs):
        """{details.get('summary', '')}
        {details.get('description', '')}
        """
        return self._make_request("{method.upper()}", "{path}", **kwargs)
'''
    return code

def generate_test_code(spec_dict: dict) -> str:
    """Generate test code from OpenAPI specification."""
    code = '''import pytest
import requests
from api_consumer import APIConsumer

class TestAPIConsumer:
    @pytest.fixture
    def api_consumer(self):
        return APIConsumer("https://petstore3.swagger.io/api/v3")
'''
    
    # Generate tests for each endpoint
    for path, methods in spec_dict['paths'].items():
        for method, details in methods.items():
            operation_id = details.get('operationId', '').replace('-', '_')
            if operation_id:
                code += f'''
    def test_{operation_id}(self, api_consumer, mocker):
        mock_request = mocker.patch('requests.Session.request')
        mock_request.return_value.status_code = 200
        mock_request.return_value.json.return_value = {{"success": True}}
        
        response = api_consumer.{operation_id}()
        assert response == {{"success": True}}
'''
    return code

if __name__ == '__main__':
    generate_api_consumer("https://raw.githubusercontent.com/swagger-api/swagger-petstore/master/src/main/resources/openapi.yaml")