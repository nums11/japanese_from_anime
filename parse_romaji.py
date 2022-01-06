"""
Creates a dictionary of all the unique romaji words in the transcript
and their english counterparts
"""
import re
import subprocess

def removeLongVowels(str):
  new_str = str
  new_str = new_str.replace("ā", "aa")
  new_str = new_str.replace("ē", "e")
  new_str = new_str.replace("ī", "i")
  new_str = new_str.replace("ō", "ou")
  new_str = new_str.replace("ū", "uu")
  return new_str

romaji_words = []
with open('episode 1/romaji.txt','r') as file:
  for line in file:
    for word in line.split():
    # just punctuation
      if re.search('[a-zA-Z]', word) == None:
        continue
      romaji_words.append(word)

# romaji_transcript = 'episode 1/romaji2.txt'

# lines = None
# with open(romaji_transcript) as f:
#   lines = f.read().splitlines()

# # print(len(lines))/

# # dialogue is every 4 lines starting at line 2
# i = 2
# while i < len(lines):
#   print(lines[i], i)
#   # dialogue.append(lines[i])

#   i += 4

unique_romaji_words = set(romaji_words)
print(unique_romaji_words, len(unique_romaji_words))

# Get the definition of each word using myougiden
# and store it in a romaji_to_english dictionary
romaji_to_english_dict = {}
unknown_words = []
count = 0
for word in unique_romaji_words:
  print("word", count)
  # Remove long vowels fromy word to work with myougiden dictionary search
  result = subprocess.run(['myougiden', '-r', removeLongVowels(word)], capture_output=True)
  if result.returncode == 0:
    definition = result.stdout.decode("utf-8")
    romaji_to_english_dict[word] = definition
  else:
    print("Unknown word", word)
    unknown_words.append(word)

  count += 1
  # if count == 10:
  #   break

print("Created Episode Dictionary of size " + str(len(romaji_to_english_dict)))
print(romaji_to_english_dict)
print("\n")
print(str(len(unknown_words)) + " words wer unknown:", unknown_words)

"""
The current problem is that there are too many unknown words.
Why are there so many unknown words? (347)
1) Some of the romaji are written with a long vowel.
- When you pass the word written this way to myougiden it can't find the word,
but when you remove it it is usually able to find it. So I could write a function
to substite long vowels with their regular characters.
- But even that's still a small percentage of the unknown words (maybe 30).
- Actually that brought it down a decent bit. The number of unknown words is now
286 so that brought it down by 61 words.

2) Some of the words only come in after the ending song. I don't really need to know this part
so I can try removing these. Doing this and pointing to the right Romaji file brought down
the # unknown words to 260

3) I think this is the biggest issue. The transcript file that I'm using has no spaces between
individual words or if it does, the spacing is inconsistent. Thus when I copy and paste it into
Romajidesu it tries finding the romaji for some combined words instead of the individual words
and ends up generating something like "hairuga" instead of "hairu" and "ga". If can get a correctly
spaced transcript file in the first place this should fix this. On animelon the subs appear to be
spaced perfectly. I could either copy them one by one into my own transcript or figure out how to
grab them from the source automatically. I did this and it's a little better but not nearly as
much as I was hoping. Unknown words is now down to 216.

4) Words are still being combined but this time it's the fault of Romajidesu. Even though I space
out each word individually it's romaji translator is still combining some of them in the romaji
translations (e.g. だけ です => dakedesu instead of dake desu). Is there a python tool to translate
japanese to romaji? If so I could do it on a word by word level and probably get much more accurate translations.
Or alternatively what if I created my dialogue file with each word only taking up one line. Would romajidesu
be more accurate then? This was it lol down to 57 unknown words. This is manageable for an anlysis
"""