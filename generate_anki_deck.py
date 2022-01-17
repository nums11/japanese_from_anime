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
  with open('episode 2/romaji.txt','r') as file:
    for line in file:
      for word in line.split():
      # just punctuation
        if re.search('[a-zA-Z]', word) == None:
          continue
        romaji_words.append(word)
  unique_romaji_words = set(romaji_words)
  print("Parsed " + str(len(unique_romaji_words)) + " unique romaji words\n")

  # Get the definition of each word using myougiden
  # and store it in a romaji_to_english dictionary
  romaji_to_english_dict = {}
  unknown_words = []
  count = 0
  print("Creating Dictionary")
  for word in unique_romaji_words:
    print("word", count)
    # Remove long vowels fromy word to work with myougiden dictionary search
    result = subprocess.run(['myougiden', '-r', removeLongVowels(word)], capture_output=True)
    if result.returncode == 0:
      definition = result.stdout.decode("utf-8")
      definition = definition.replace('\t', '\n\n')
      romaji_to_english_dict[word] = definition
    else:
      print("Unknown word", word)
      unknown_words.append(word)
    count += 1

  print("Created Episode Dictionary of size " + str(len(romaji_to_english_dict)))
  print("\n")
  print(str(len(unknown_words)) + " words were unknown:", unknown_words)
  return romaji_to_english_dict

def generateAnkiDeck(romaji_to_english_dict):
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

  package_name = "naruto_episode_1.apkg"
  genanki.Package(my_deck).write_to_file(package_name)
  print("\nAnki deck generated: " + package_name)

# romaji_to_english_dict = createRomajiToEnglishDict()
# generateAnkiDeck(romaji_to_english_dict)

romaji_words_one = []
with open('episode 1/romaji.txt','r') as file:
  for line in file:
    for word in line.split():
    # just punctuation
      if re.search('[a-zA-Z]', word) == None:
        continue
      romaji_words_one.append(word)
unique_romaji_words_one = set(romaji_words_one)
print("Num words episode 1:", len(unique_romaji_words_one))

romaji_words_two = []
with open('episode 2/romaji.txt','r') as file:
  for line in file:
    for word in line.split():
    # just punctuation
      if re.search('[a-zA-Z]', word) == None:
        continue
      romaji_words_two.append(word)
unique_romaji_words_two = set(romaji_words_two)
print("Num words episode 2:", len(unique_romaji_words_two))

print("Num new words in episode 2:", sum(el in unique_romaji_words_one for el in unique_romaji_words_two))
print(len(set(romaji_words_one + romaji_words_two)))


print(len(unique_romaji_words_one | unique_romaji_words_two))
# unique_romaji_words = set(romaji_words_one)
# print("Parsed " + str(len(unique_romaji_words)) + " unique romaji words\n")


"""
Instead of learning the new words for each episode. I can just learn the most common words
in order of frequency for the whole show.... And I can set a goal along this  (maybe 10 a day).

So 1 part is doing this, and the second part is doing the subtitle tutor - 1 episode a day in sub
then without sub. doing this for a few months and seeing how it goes. This helps me answer the question
of learning new vocab and still keeps the focus on listening. I still question if I even need to watch the
episode twice because I've already seen it but I'll give it a try.

He got away with not really looking anything up.

Definitely feel like I should watch the episode twice back to back. It can be a little mundande the second time
but it does give the greater illusion that I know more of the dialogues since I just heard them and I can listen
with the goal of really picking out every word.
"""