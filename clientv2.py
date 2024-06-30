import requests
import json

# Replace with the server URL
SERVER_URL = 'https://tiered-web-app-fe-vtu34wdxea-ul.a.run.app/'

def send_get_request():
    try:
        response = requests.get(SERVER_URL)
        if response.status_code == 200:
            print(f"GET request successful: {response.text}")
        else:
            print(f"GET request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred during GET request: {e}")

def send_post_request(data):
    try:
        headers = {'Content-Type': 'application/json'}
        response = requests.post(f"{SERVER_URL}/data", headers=headers, data=json.dumps(data))
        if response.status_code == 200:
            print(f"POST request successful: {response.text}")
        else:
            print(f"POST request failed with status code: {response.status_code}")
    except Exception as e:
        print(f"An error occurred during POST request: {e}")

if __name__ == "__main__":
    # Send a GET request
    send_get_request()

    # Prepare data to be sent in the POST request
    data_to_send = {
        'key1': 'value1',
        'key2': 'value2'
    }

    # Send a POST request with the data
    send_post_request(data_to_send)
