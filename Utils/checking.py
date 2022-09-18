"""Metods for cheking responses"""
import json
from requests import Response

class Checking():

    """method for checking status codes"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f'Passed!!! Status code = {response.status_code}')
        else:
            print(f'Failed!!! Status code = {response.status_code}')

    """method for checking main fields in response"""
    @staticmethod
    def check_json_token(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('All response fields are presented')

    """method for checking fields value in response"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(field_name, 'field checking -------- PASSED')

    """method for checking fields value in response by search word"""
    @staticmethod
    def check_json_search_word_in_value(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print('Word -- ', search_word, '---- in value is presented')
        else:
            print('Word -- ', search_word, '---- not found')