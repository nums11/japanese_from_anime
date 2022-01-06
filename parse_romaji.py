"""
Creates a dictionary of all the unique romaji words in the transcript
and their english counterparts
"""
import re
import subprocess

romaji_words = []
with open('episode 1/romaji2.txt','r') as file:
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

romaji_to_english_dict = {}
unknown_words = []
count = 0
for word in unique_romaji_words:
  print("word", count)
  result = subprocess.run(['myougiden', '-r', word], capture_output=True)
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

# result = subprocess.run(['myougiden', '-r', 'hajimeru'], capture_output=True)
# result_str = result.stdout.decode("utf-8") 
# print(result_str)

# if result.returncode == 0:
#   output = result.stdout.split(b'\t') # split byte string by tabs
#   for line in range(len(output)):
#     print(line, output[line])
# else:
#   print("Unknown word")
# print(result)
# output = re.split(r'\t+', output)
# formatted_output = output.stdout.split(b'\t')
# print(formatted_output[2])