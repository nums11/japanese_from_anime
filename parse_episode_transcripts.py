"""
Parse the episode transcript to generate a file that only
has the Japanese dialogue
"""

import re

def lineIsDialogue(line):
  if not re.search('[a-zA-Z]', line) == None:
    return False
  if any(char.isdigit() for char in line):
    return False
  if len(line) == 0:
    return False
  return True

all_episode_dialogues = []

for i in range(1,221):
  episode_transcript = '../Naruto [Formatted, fixed 0-220].jpn.sub/Naruto (' + str(i) + ').srt'
  print("Parsing", episode_transcript)

  # Read transcript file
  lines = None
  with open(episode_transcript) as f:
    lines = f.read().splitlines()

  dialogue = [x for x in lines if lineIsDialogue(x)]
  dialogue.insert(0, 'Episode ' + str(i) + '\n')
  dialogue.append('\n')

  all_episode_dialogues.append('\n'.join(dialogue))

# Write to the output file
output_file = open('naruto_episode_dialogues.txt', 'w')
output_file.write('\n'.join(all_episode_dialogues))
output_file.close()

print("All episode transcripts parsed")