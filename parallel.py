"""
Matthew Farias
104600696

"""

import multiprocessing as mp
import Levenshtein as lev
import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn


class Word:
    """Word object that hold 2 attributes word and dist
        word->string
        dist->int
        for comparisons 
    """
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

#Loading in data from birbeck files
birbeck=[]
file1 = open('data/FAWTHROP1DAT.643')
for line in file1:
    birbeck.append(line.lower().split())
file1.close()

file2 = open('data/SHEFFIELDDAT.643')
for line in file2:
    birbeck.append(line.split())
file2.close()



def best_k_words(line):
    """Calculates the distance between the incorrect spelling and all words in wordnet.

    :param line: array with incorrect and correct word
    :return: returns k Word objects with the lowest distance to the incorrect word
    """
    k=10
    wrong_word=line[0].lower()
    all_words=wn.words(lang='eng')
    top_current=[]
    for word in all_words:
        if len(top_current)<k:
            top_current.append(Word(wrong_word,lev.distance(word,wrong_word)))
            if len(top_current)==k:
                top_current.sort(reverse=True)
        else:
            new_dist=lev.distance(word,wrong_word,score_cutoff=top_current[0].dist)
            if new_dist<top_current[0].dist:
                top_current[0]=Word(word,new_dist)
                top_current.sort(reverse=True)
    return top_current


#using multiprocessing to find Lev distances faster
top_all=[]
pool=mp.Pool()
top_all.append(pool.map(best_k_words,birbeck))    
top_all=top_all[0]


k1_score=0
k5_score=0
k10_score=0

word_cnt=len(birbeck)

#Calculating s@k for k=1,5,10
for i in range(word_cnt):
    right_word=birbeck[i][1].lower()
    for j in range(9,-1,-1):
        if top_all[i][j].word==right_word:
            if j>8:
                k1_score+=1
                k5_score+=1
            elif j>4:
                k5_score+=1
            k10_score+=1
            break


#Getting average score
k1_score=k1_score/word_cnt
k5_score=k5_score/word_cnt
k10_score=k10_score/word_cnt

#print results
print('s@k=1: ',k1_score, '\ns@k=5: ',k5_score,'\ns@k=10:',k10_score)


