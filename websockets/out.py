text_a = open("input1.txt").read()
text_b = open("input1.txt").read()

import random
import pronouncing
import os
from os import system
import markovify
import subprocess
import itertools

class SentencesByChar(markovify.Text):
    def word_split(self, sentence):
        return list(sentence)
    def word_join(self, words):
        return "".join(words)


  # change to "word" for a word-level model
level = "word"
# controls the length of the n-gram
order = 7
# controls the number of lines to output
output_n = 1
# weights between the models; text A first, text B second.
# if you want to completely exclude one model, set its corresponding value to 0
weights = [0.3, 0.7]
# limit sentence output to this number of characters
length_limit = 40


while True:
        for _ in itertools.repeat(None, 1):
        	model_cls = markovify.Text if level == "word" else SentencesByChar
        	gen_a = model_cls(text_a, state_size=order)
        	gen_b = model_cls(text_b, state_size=order)
        	gen_combo = markovify.combine([gen_a, gen_b], weights)
        	counter=0
        	for i in range(output_n):
        		out = gen_combo.make_short_sentence(length_limit, test_output=False)
        		out = out.replace("\n", " ")
        		print(out)
        	import pronouncing
        	import random
        	import time
        	text = out
        	outs = list()
        	for word in text.split():
        			rhymes = pronouncing.rhymes(word)
        			if len(rhymes) > 0:
        				outs.append(random.choice(rhymes))
        			else:
        				outs.append(word)
        	print(' '.join(outs))
        	time.sleep(3)

