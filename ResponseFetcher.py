import requests

class ColabResponseFetcher:
    def __init__(self, url):
        self.url = url

    def fetch(self, message):
        data = {'key': message}
        response = requests.post(self.url, json=data)
        return response.text
    
if __name__ == '__main__':
    fetcher = ColabResponseFetcher('http://a1f0-34-34-27-89.ngrok-free.app/receive_data')
    print(fetcher.fetch('hello world'))