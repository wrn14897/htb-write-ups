import requests


def main():
    resp = requests.post(
        'http://157.245.40.149:31208/index.php',
        json={
            'user': '!'
        }
    )
    print(resp.text)


if __name__ == '__main__':
    main()
