#coding=utf-8

## this file is to load the model and output word vector

from gensim.models import Doc2Vec
import numpy as np
import gensim

model = gensim.models.Word2Vec.load('/home/guanxinjun/word2vec/zhwiki.model')
#model = Doc2Vec.load_word2vec_format('zhwiki.vector',binary=False)

def get_word_vector(word):
	if type(word) != unicode:
		word = word.decode('utf-8')
	if word in model.vocab:
		return model[word]
	else:
		return np.zeros((1,400),dtype=np.float32)

def get_sentence_vector(sentence):
	vector = np.zeros((1,400),dtype=np.float32)
	if len(sentence) == 0: return vector
	for word in sentence:
		vector = np.add(vector,get_word_vector(word))
	mean = vector / len(sentence)
	return mean.tolist()


if __name__ == '__main__':
	#string = raw_input('word')
	#string = string.decode('utf-8')
	#print model[string]
	get_sentence_vector(['今天','肚子','饿'])
