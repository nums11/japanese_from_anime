"""
Creates Romaji -> English Anki cards
"""
import re
import subprocess
import genanki
import random
# print(random.randrange(1 << 30, 1 << 31))

def removeLongVowels(str):
  new_str = str
  new_str = new_str.replace("ā", "aa")
  new_str = new_str.replace("ē", "e")
  new_str = new_str.replace("ī", "i")
  new_str = new_str.replace("ō", "ou")
  new_str = new_str.replace("ū", "uu")
  return new_str

def createRomajiToEnglishDict():
  # Create a set of the unique romaji words
  romaji_words = []
  with open('episode 1/romaji.txt','r') as file:
    for line in file:
      for word in line.split():
      # just punctuation
        if re.search('[a-zA-Z]', word) == None:
          continue
        romaji_words.append(word)
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

  print("Created Episode Dictionary of size " + str(len(romaji_to_english_dict)))
  print("\n")
  print(str(len(unknown_words)) + " words were unknown:", unknown_words)
  return romaji_to_english_dict

romaji_to_english_dict = {}
for i in range(10):
  romaji_to_english_dict["Romaji " + str(i)] = "English " + str(i)

my_model = genanki.Model(
  1407607172,
  'Simple Model',
  fields=[
    {'name': 'Question'},
    {'name': 'Answer'},
  ],
  templates=[
    {
      'name': 'Romaji To English',
      'qfmt': '{{Question}}',
      'afmt': '{{FrontSide}}<hr id="answer">{{Answer}}',
    },
  ])

my_deck = genanki.Deck(
  1170750336,
  'Naruto Episode 1 Vocab')

for romaji, english in romaji_to_english_dict.items():
  my_deck.add_note(
    genanki.Note(
      model=my_model,
      fields=[romaji, english]
    )
  )

genanki.Package(my_deck).write_to_file('naruto_episode_1.apkg')