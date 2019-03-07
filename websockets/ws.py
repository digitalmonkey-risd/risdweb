#!/usr/bin/env python

# WS server that sends messages at random intervals
text_a = open("input1.txt").read()
text_b = open("input1.txt").read()

import asyncio
import random
import websockets
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
length_limit = 90


async def time(websocket, path):
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
        now = out
        await websocket.send(now)
        await asyncio.sleep(5.5)


start_server = websockets.serve(time, '127.0.0.1', 5678)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()

