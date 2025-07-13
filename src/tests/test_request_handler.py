import pytest
from unittest.mock import patch
from src.request_response.request_handler import get_authorization, post_application


@patch("src.request_response.request_handler.requests.get")
def test_get_authorization(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {"result": "sample"}

    token = get_authorization("https://test.com")
    assert token == "sample"


@patch("src.request_response.request_handler.requests.post")
def test_post_application(mock_post):
    mock_post.return_value.status_code = 200
    mock_post.return_value.text = "Success"

    payload = {"name": "Test", "*final_attempt": True, "**extra_information": {"Years of Experience": "9"}}
    post_application("https://test.com", "sample", payload)

    mock_post.assert_called_once()


@patch("src.request_response.request_handler.requests.post")
def test_post_application_invalid_input(mock_post):
    mock_post.return_value.status_code = 422
    mock_post.return_value.text = "Invalid Input"

    payload = {"name": "Test", "*final_attempt": "9", "**extra_information": {"Years of Experience": "9"}}
    response = post_application("https://test.com", "sample", payload)
    assert response.text == "Invalid Input"
    mock_post.assert_called_once()