import requests

base_url = "https://api.twitch.tv/kraken/"

#This should be changed.
CLIENT_ID = "kagylf8s6cs0mrqo6qzpvn6t3moffvs"


headers = {'Accept': 'application/vnd.twitchtv.v3+json', 'Client-ID': CLIENT_ID}

def is_online(username):
    data = get_stream_status(username)
    return (data['stream'] is not None)

def get_stream_status(username):
    url = base_url + "streams/{}".format(username)
    resp = requests.get(url, headers=headers)
    data = resp.json()
    
    return data
