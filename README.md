# John-Madden-Bot
Generates John Madden sound-alike quotes and posts them to Twitter.

Came up with the idea as a joke, followed through as a way to learn new libraries and write some OO-looking code.

Libraries used:
bs4
markovify
tweepy

Contents:
main.py - Fetches a sentence from the markov model and posts it on twitter
markov.py - Generates the markov chain model, returns sentences
scrapequotes.py - Scrapes a site for quotes
twitterapi.py - Interface for connecting and posting to Twitter
docs/jmcorpus.txt - Line-delimited corpus of John Madden quotes
