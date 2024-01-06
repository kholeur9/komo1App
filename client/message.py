import requests
import os

api_key = os.environ['API_KEY_TECH']

def demande_credit(message):

    sms_body = {
        'action': 'send-sms',
        'api_key': api_key,
        'to': '24174871292',
        'from': 'TECHSOFT',
        'sms': message,
    }

    api_url = "https://app.techsoft-web-agency.com/sms/api"
    try:
        response = requests.post(api_url, data=sms_body)
        return response.text
    except Exception as e:
        print(e)
        return "Error"