import collections
import re

romaji_words = []
with open('naruto_episode_romaji.txt','r') as file:
  for line in file:
    for word in line.split():
      if re.search('[a-zA-Z]', word) == None:
        continue
      romaji_words.append(word)

counter=collections.Counter(romaji_words)
print(counter.most_common(100))
# num_words = 10
# for key, value in counter.items():
#   print(key, value)
