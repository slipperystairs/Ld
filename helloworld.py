import tweepy, time, sys

argfile = str(sys.argv[1])

CONSUMER_KEY = 'dPwYmO06udcsjTUSrb20OTFDg'
CONSUMER_SECRET = 'bmYgOURpsuz48NZZITGXbtQlogS2DlAiPvv74gWZGtcisGNCMm'
ACCESS_KEY = '4878629961-A1L2k1IVKotZKT90NGIw0Q3WLmyl1bYhcEAZnKP'
ACCESS_SECRET = 'dOAkSXkieIBNa7renyop6qIlu0k2oxEbSKUoC7vUBgSUO'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

filename = open(argfile, 'r')
f = filename.readlines()
filename.close()

for line in f:
	api.update_status(line)
	time.sleep(900)#Tweets ever 15 minutes