import random
import os

paths = os.path.join(os.getcwd(), "applications", "markov", "input.txt")

# Read in all the words in one go
with open(paths) as f:
    words = f.read()

# TODO: analyze which words can follow other words
# Your code here
print("words")
print(words)
split = words.split(" ")
dict = {}

for index, word in enumerate(split):
    if word not in dict:
        dict[word] = set()
    if index + 1 >= len(split) -1:
        break
    dict[word].add(split[index + 1])

print(dict)


# TODO: construct 5 random sentences
# Your code here

