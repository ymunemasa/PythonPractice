import json
from tweepy import OAuthHandler, Stream, API
from tweepy.streaming import StreamListener

consumer_key = 'WSmtV47JmvlllxOX98tO0Zdgw'
consumer_secret = 'cvNlgP6cpnqXQ93mPvrBKgF6JWGhMOesNHiBM6sllUZCybvgOo'
access_token = '1001853217-Sc5SRifh8etvZfNNYKzMweHbKuRvID91Jmfu2Sk'
access_token_secret = 'KhrJw1bYPuVM0jyHGguFSTbgtBzUIg9PFYNXDPqOt2HpE'

auth = OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token, access_token_secret)

class PrintListener(StreamListener):
    def on_status(self, status):
        if not status.text[:3] == 'RT ':
            print(status.text)
            print(status.author.screen_name,
                status.created_at,
                status.source,
                '\n')

    def on_error(self, status_code):
        print("Error code: {}".format(status_code))
        return True #keep stream arive

    def on_timeout(self):
        print('Listener timed out!')
        return True #keep stream alive

def print_to_terminal():
    listener = PrintListener()
    stream = Stream(auth, listener)
    languages = ('en',)
    stream.sample(languages=languages)

def  pull_down_tweets(screen_name):
    api = API(auth)
    tweets = api.user_timeline(screen_name=screen_name, count=200)
    for tweet in tweets:
        print(json.dumps(tweet._json, indent=4))

if __name__ == '__main__':
    #print_to_terminal()
    pull_down_tweets(auth.username)
