import requests


class WebAPIClient:
    def __init__(self):
        self.base_url = 'http://127.0.0.1:5000'  # Update with your Web API URL

    def upload_file(self, file_path):
        url = f'{self.base_url}/upload'
        files = {'file': open(file_path, 'rb')}
        response = requests.post(url, files=files)
        data = response.json()
        return data.get('uid')

    def get_status(self, uid):
        url = f'{self.base_url}/status/{uid}'
        response = requests.get(url)
        return response.json()
