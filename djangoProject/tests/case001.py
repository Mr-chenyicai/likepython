import requests, pprint

payload = {
    'username': 'byhy',
    'password': '88888888'
}

response = requests.post('http://127.0.0.1:8000/mgr/signin.html',
              data=payload)

pprint.pprint(response.json())