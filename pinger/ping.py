import responses
import httplib2
from time import sleep
from pyenv import ENV
from local_settings import TIMEOUT, URL
from requests.exceptions import HTTPError
import sys


ENV.TIMEOUT = TIMEOUT
ENV.URLS = URL

class Ping:
    def __init__(self, urls):
        self.urls = urls

    def run(self):
        sleep(ENV.TIMEOUT) # sec
        for url in self.urls:
            connect = httplib2.HTTPConnectionWithTimeout(url)
            connect.request("GET", "/")
            c = connect.getresponse()
            print(url, c.status, c.reason)
        print("Call & Wake up url")


if __name__ == '__main__':
    while True:
        try:
            ping = Ping(ENV.URLS)
        except KeyboardInterrupt:
            sys.exit()
        except Exception as e:
            print(e)
        