import os
import random

arr = []

WORDS = open("word").read().splitlines()

for i in range(12):
    arr.append(random.choice(WORDS))

seed_phrase = " ".join(arr)

print(seed_phrase)