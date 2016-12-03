import requests

headers = {'Accept': 'application/vnd.twitchtv.v3+json', 'Client-ID': 'kagylf8s6cs0mrqo6qzpvn6t3moffvs'}
url = 'https://api.twitch.tv/kraken/search/streams'
userinput = input()
payload = {}
payload['q'] = userinput
r = requests.get( url , params=payload, headers=headers)
data = r.json()

print (data)
