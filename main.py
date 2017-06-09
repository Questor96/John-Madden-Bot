from twitterapi import TwitterAPI
from markov import MarkovModel

POST_SIGNATURE = ' #JohnMaddenBot'

if __name__ == '__main__':
    #get something to post
    johnMadden = MarkovModel('docs/jmcorpus.txt')
    postContent = johnMadden.makeSentence(140-len(POST_SIGNATURE)) + POST_SIGNATURE

    #set up twitter connection
    tweeter = TwitterAPI('tokens.txt')
    tweeter.tweet(postContent)
