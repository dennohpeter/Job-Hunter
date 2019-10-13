import requests
import base64
from django.conf import settings


class SMS:
    """
    SMS Context 

    """
    # Retrieving Credentials
    API_KEY = settings.API_KEY
    CONSUMER_SECRET = settings.CONSUMER_SECRET
    PROJECT_ID = settings.PROJECT_ID
    BASE_URL = settings.BASE_URL

    def send_sms(self, phone_number, message):
        response = requests.post(self._telerivet_url(), json=self._request_body(
            phone_number, message), headers=self._headers())
        return response.json()

    def _telerivet_url(self):
        return "%s/%s/messages/send" % (self.BASE_URL, self.PROJECT_ID)

    def _request_body(self, phone_number, message):
        body = {
            "content": message,
            "to_number": phone_number,
        }
        return body

    def _headers(self):
        headers = {
            "Content-type": "application/json",
            "Authorization": "Basic %s" % self._encoded_key()
        }
        return headers

    def _encoded_key(self):
        key_str = self.API_KEY + ":" + self.CONSUMER_SECRET
        key_bytes = key_str.encode('utf-8')
        key_str = base64.b64encode(key_bytes).decode('utf-8')
        return key_str
