from requests import Session


MAX_ITEMS_PER_REQ = 100



class TwitchAPI():
    sess = Session()
    base_url = 'https://api.twitch.tv/kraken'
    headers = {'Accept': 'application/vnd.twitchtv.v3+json', }
    
    def __init__(self, client_id):
        self.headers['Client-ID'] = client_id

    
    def is_online(self, username):
        stream_data = self.get_stream_status(username)

        #If the user is not found, return None
        if 'stream' not in stream_data.keys():
            return None

        return (stream_data['stream'] is not None)

    
    def get_stream_status(self, username):
        url = self.base_url + '/streams/{}'.format(username)
        resp = self.sess.get(url, headers=self.headers)
        stream_status = resp.json()

        return stream_status


    #Note: The two following methods make no use of twitch's authentication
    #      option. This is bad and it should change.
    #TODO: Enable Authentication and use it instead of this ugly mess.
    def get_live_followed_streams(self, my_username):
        followed_streams = self.get_followed_streams(my_username)
        live_followed_streams = []
        for stream in followed_streams:
            if self.is_online(stream['channel']['name']):
                live_followed_streams.append(stream)

        return live_followed_streams
        
    
    def get_followed_streams(self, my_username):
        url = self.base_url + '/users/{}/follows/channels?limit={}'.format(my_username, MAX_ITEMS_PER_REQ)
        resp = self.sess.get(url, headers=self.headers)
        data = resp.json()
        followed_streams = data['follows']

        total = data['_total']
        for items_recieved in range(MAX_ITEMS_PER_REQ, data['_total'], MAX_ITEMS_PER_REQ):
            resp = self.sess.get(data['_links']['next'], headers=self.headers)
            data = resp.json()
            followed_streams += data['follows']
        
        return followed_streams
