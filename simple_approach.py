"""
Matthew Farias
104600696

"""

from math import dist
import Levenshtein as lev
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn


class Word:
    def __init__(self, word, dist) -> None:
        self.word=word
        self.dist=dist
    def __lt__(self, other):
        return self.dist<other.dist
    def __le__(self, other):
        return self.dist<=other.dist
    def __ge__(self, other):
        return self.dist>=other.dist
    def __gt__(self, other):
        return self.dist>other.dist
    def __eq__(self, other):
        return self.dist==other.dist
    def __repr__(self) -> str:
        return self.word + ", "+str(self.dist)

words1=[]
file1 = open('data/FAWTHROP1DAT.643')
for line in file1:
    words1.append(line.split())
file1.close()

file2 = open('data/SHEFFIELDDAT.643')
for line in file2:
    words1.append(line.split())
file2.close()

top_all=[]

k=5
cnt=0
for line in words1:
    wrong_word=line[1].lower()
    top_current=[]
    print('Current Word is:',wrong_word)
    for word in wn.words(lang='eng'):
        if len(top_current)<k:
            top_current.append(Word(wrong_word,lev.distance(word,wrong_word)))
            if len(top_current)==k:
                top_current.sort(reverse=True)
        else:
            new_dist=lev.distance(word,wrong_word,score_cutoff=top_current[0].dist)
            if new_dist<top_current[0].dist:
                top_current[0]=Word(word,new_dist)
                top_current.sort(reverse=True)
    top_all.append(top_current)
    print('Top K are:', top_current)
    cnt+=1

    
