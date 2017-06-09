import tweepy

class TwitterAPI:

    def __init__(self,tokenFile):
        with open(tokenFile,'r') as file:
            CONSUMER_KEY = self.__getTokenFromLine(file)
            CONSUMER_SEC = self.__getTokenFromLine(file)
            ACCESS_TOKEN = self.__getTokenFromLine(file)
            ACCESS_SECRET = self.__getTokenFromLine(file)

        auth = tweepy.OAuthHandler(CONSUMER_KEY,CONSUMER_SEC)
        auth.set_access_token(ACCESS_TOKEN,ACCESS_SECRET)

        self.api = tweepy.API(auth)
    
    def __getTokenFromLine(self,file):
        return file.readline().split('\t')[1].strip()

    def tweet(self, message):
        self.api.update_status(status=message)

if __name__ == '__main__':
    twitter = TwitterAPI('tokens.txt')
    twitter.tweet('test message')
