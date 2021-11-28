import hashlib
import requests
from bs4 import BeautifulSoup

url = 'http://167.71.140.171:30361'

'''
    This method will scrap input string from the index page
    and send its MD5 hash value back to target API

    key -> using session
'''


def main():
    s = requests.Session()
    req = s.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    inputString = soup.h3.text
    print(f'input string: {inputString}')
    req = s.post(
        url,
        data={'hash': hashlib.md5(inputString.encode()).hexdigest()},
    )

    print(req.text)


if __name__ == '__main__':
    main()
