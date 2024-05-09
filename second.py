import requests

# Global variables
access_token = ''
refresh_token = ''
client_id = '<client_id>'
client_secret = '<client_secret>'

def get_logs():
    # The URL you're making the GET request to
    url = ''

    # The headers for the GET request
    headers = {
        'Authorization': f'Bearer {access_token}'
    }

    # Make the GET request
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data
    elif response.status_code == 401:
        if refresh_access_token():
            return get_logs()


def refresh_access_token():
    url = ''
    data = {
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token',
        'refresh_token': refresh_token
    }
    response = requests.post(url, data=data)
    
    if response.status_code == 200:
        new_token_data = response.json()
        global access_token
        access_token = new_token_data['access_token']
        global refresh_token
        refresh_token = new_token_data['refresh_token']
        return True
    else:
        print('Failed to refresh access token')
        return False