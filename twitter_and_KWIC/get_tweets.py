import tweepy
import secret_config as conf

KEYS = ['ワタシ','アタシ','オレ','ボク','ワタクシ','わたし','あたし','おれ','ぼく','わたくし']

consumer_key = conf.consumer_key
consumer_secret_key = conf.consumer_secret_key

access_token = conf.access_token
access_token_secret = conf.access_token_secret

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

f = open('raw_tweets.txt', 'a', encoding='utf8')

class JPStreamer(tweepy.StreamListener):

    def on_error(self, status_code):
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False

    def on_status(self, status):
        print(status.text)
        f.write(status.text)
        f.write('<NEWTWEET>')

jp_streamer = JPStreamer()
jp_stream = tweepy.Stream(auth=api.auth, listener=jp_streamer)

jp_stream.filter(track=KEYS, languages=["ja"])

f.close()