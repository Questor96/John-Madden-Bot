import markovify

class MarkovModel:
    def __init__(self,filename):
        with open(filename) as file:
            self.corpus = file.read()
        self.model = markovify.NewlineText(self.corpus)


    def makeSentence(self,length = 0):
        if length > 0:
            return self.model.make_short_sentence(length)
        else:
            return self.model.make_sentence()

if __name__ == '__main__':
    john_madden = MarkovModel('docs/jmcorpus.txt')
    print(john_madden.makeSentence())
    print(john_madden.makeSentence(40))
