import requests

from constants.api_endpoint import API_GET_ALL_BUILDS, API_LOGIN

class RequestsApi:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()
        
    def login(self, email, password):
        return requests.post(f"{self.base_url}{API_LOGIN}", data={"email": email, "password": password})
    
    def get_all_builds(self):
        return (requests.get(f"{self.base_url}{API_GET_ALL_BUILDS}")).json()
    