import requests

class ColabResponseFetcher:
    def __init__(self, url):
        self.url = url

    def fetch(self, message):
        data = {'key': message}
        response = requests.post(self.url, json=data)
        return response.text
    
if __name__ == '__main__':
    fetcher = ColabResponseFetcher('http://927e-35-204-93-188.ngrok-free.app/receive_data')
    print(fetcher.fetch('hello world'))