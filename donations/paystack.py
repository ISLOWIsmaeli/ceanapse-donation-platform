import json
import requests
from django.conf import settings

def checkout(payload):
    headers = {
        "Authorization": f"Bearer {settings.PAYSTACK_TEST_SECRET_KEY}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        settings.PAYSTACK_INITIALIZE_PAYMENT_URL,
        headers=headers, 
        data=json.dumps(payload)
    )
    response_data = response.json() 
    print(response_data)

    if response_data.get('status') == True:
        return True, response_data['data']['authorization_url'], response_data
    else:
        return False, "Failed to initiate payment, please try again later.",response_data