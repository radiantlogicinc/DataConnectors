# Application Specifications

## Overview
This application takes a REST API specification via a URL and generates code for a class that serves as a consumer of that REST API. This class will implement methods to consume every method exposed by the REST API. Along with the consumer class, it will also generate a pytest in a separate file to test the methods of the consumer class.

## Function Specifications

### `generate_api_consumer(api_spec_url: str) -> None`
- **Description**: Generates a REST API consumer class and corresponding test file
- **Parameters**:
  - `api_spec_url` (str): URL to the REST API specification
- **Returns**:
  - None: Creates files in the current directory
- **Output Files**:
  - `api_consumer.py`: Contains the generated API consumer class
  - `test_api_consumer.py`: Contains pytest tests for the consumer class

## Testing
The application includes a comprehensive test suite using pytest that verifies:
1. The generated consumer class correctly implements all API endpoints
2. The generated test file provides adequate test coverage
All tests must pass before any changes are merged.

## Requirements
- Python 3.8+
- pytest (for testing)
- requests (for API interaction)
- openapi-spec-validator (for API spec validation)

## File Structure
```
DataConnectors/
├── api_consumer.py
├── test_api_consumer.py
├── main.py
└── documentation/
    └── app_spec.md
```