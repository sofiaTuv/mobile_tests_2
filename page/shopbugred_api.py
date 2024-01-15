import json
import logging
import os
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from dotenv import load_dotenv

load_dotenv()
WEB_URL = os.getenv('WEB_URL')
API_URL = os.getenv('API_URL')


class TestShopBugredAPI:

    @staticmethod
    @step('API Request')
    def api_request(url, **kwargs):
        result = requests.post(url=API_URL + url, **kwargs)
        TestShopBugredAPI.attach_request_info(result)
        return result

    @staticmethod
    @step('Attach Request Info')
    def attach_request_info(result):
        allure.attach(result.request.url, name="Request url", attachment_type=AttachmentType.TEXT)
        allure.attach(json.dumps(result.request.body, indent=4, ensure_ascii=True),
                      name="Request body", attachment_type=AttachmentType.JSON, extension="json")
        allure.attach(json.dumps(result.json(), indent=4, ensure_ascii=True),
                      name="Response", attachment_type=AttachmentType.JSON, extension="json")

        logging.info(f'Request: {result.request.url}')
        logging.info(f'INFO Request body: {result.request.body}')
        logging.info(f'Request headers:  {result.request.headers}')
        logging.info(f'Response code: {result.status_code}')
        logging.info(f'Response: {result.text}')
