import collections
import re
import genanki

# romaji_words = []
# with open('naruto_episode_romaji.txt','r') as file:
#   for line in file:
#     for word in line.split():
#       if re.search('[a-zA-Z]', word) == None:
#         continue
#       romaji_words.append(word)

# counter=collections.Counter(romaji_words)
# most_common = counter.most_common(200)
# for tuple in most_common[100:]:
#   print(tuple[0], tuple[1], '\n')
# num_words = 10

word_dict = {
  "ore": "I; me; rough or arrogant sounding first-poerson pronoun",
  "nani": "what",
  "kono": "this",
  "koto": "thing",
  "omae": "you; sometimes derogatory",
  "kore": "this",
  "sore": "that (near somebody)",
  "sono": "that noun (near somebody)",
  "ano": "that noun (away)",
  "nda": "the reason is that...; the fact is that...; it is that...",
  "suru": "to do",
  "kara": "from; because; after",
  "dō": "how",
  "shita": "below; bottom; down",
  "demo": "but",
  "boku": "I (masculine)",
  "sō": "it seems",
  "nai": "not; no",
  "made": "until",
  "ji": "hour o'clock",
  "sato": "village",
  "jutsu": "art; technique",
  "koko": "here",
  "ichi": "one",
  "oto": "sound; noise",
  "fu": "two",
  "dake": "only; just",
  "daija": "big snake; serpent",
  "yatsu": "he; she; him (derogatory)",
  "sonna": "such",
  "sensei": "teacher",
  "mono": "person; thing; object",
  "aru": "to be",
  "rai": "next...",
  "toki": "time; moment; occasion",
  "gai": "guy",
  "hi": "day",
  "shi": "four",
  "naru": "to grow; to attain",
  "kage": "shadow",
  "shite": "by",
  "datte": "after all; because",
  "koitsu": "this one; this guy",
  "ninmu": "mission; duty",
  "konna": "such",
  "naka": "inside; among; during",
  "aitsu": "that guy",
  "chikara": "force; power",
  "jibun": "myself; yourself; oneself; himself",
  "tame": "purpose; object; result",
  "mada": "not yet",
  "nante": "what!?; how!?",
  "are": "that (over there)",
  "oi": "hey!",
  "shiro": "white",
  "nande": "why? how?",
  "hito": "man; person; human",
  "dare": "who",
  "nanda": "what!",
  "minna": "everyone; everything",
  "uwa": "Wow! Omg!",
  "shika": "only; nothing but",
  "un": "yea",
  "fun": "minute",
  "kimi": "you",
  "iya": "no",
  "kuni": "country; region",
  "dakara": "therefore",
  "yori": "from; than",
  "subete": "all; the whole; overall; in general",
  "toiu": "said; it's called",
  "saru": "a certain; to leave; monkey",
  "nan": "what",
  "anta": "you (familiar form of anata)",
  "hō": "way",
  "mae": "before; previously",
  "doko": "where",
  "anata": "you",
  "oretachi": "we; us",
  "yume": "dream",
  "shūgyō": "execution; performance",
  "sā": "well; who knows",
  "uchi": "one's house; inside; while",
  "zettai": "absolutely",
  "bunshin": "clone",
  "baka": "idiot",
  "mata": "again; and also",
  "onaji": "same",
  "chotto": "somewhat; just; a little bit",
  "kokoro": "mind; heart; spirit",
  "nakigoe": "cry",
  "teki": "opponent; rival; adversary",
  "tokoro": "place; spot",
  "karada": "body",
  "toshite": "as for; apart from",
  "nanka": "something like...; kind of...",
  "tada": "ordinary",
  "sakki": "some time ago",
  "chū": "kiss",
  "washi": "I; me (used by elderly males)",
  "janē": "see you; bye"
}

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
    'Naruto Most Common Words')

  for romaji, english in romaji_to_english_dict.items():
    my_deck.add_note(
      genanki.Note(
        model=my_model,
        fields=[romaji, english]
      )
    )

  package_name = "naruto_most_common_words.apkg"
  genanki.Package(my_deck).write_to_file(package_name)
  print("\nAnki deck generated: " + package_name)

generateAnkiDeck(word_dict)
