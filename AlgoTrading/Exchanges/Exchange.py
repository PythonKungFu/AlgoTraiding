import requests

class Exchange:
    base_url = ''


    def any_request(self, method, params=None):
        return requests.get(self.base_url + method, params=params).json()

    def exchange_info(self):
        return self.any_request(method=None)