import requests as rq

class API:
    
    API_URL = ""

    def __init__(self, api_link):
        self.API_URL = api_link
    
    def Post(self, data):
        response = rq.post(url = self.API_URL, data=data)