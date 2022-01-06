"""
Parse the episode transcript to generate a file that only
has the Japanese dialogue
"""

import re

episode_transcript = '../Naruto [Formatted, fixed 0-220].jpn.sub/Naruto (1).srt'

# Read transcript file
lines = None
with open(episode_transcript) as f:
  lines = f.read().splitlines()

# Dialogue is every 4 lines starting at line 2
dialogue = []
i = 2
while i < len(lines):
  dialogue.append(lines[i])
  i += 4

# Remove English (usually from theme song)
dialogue_no_english = [x for x in dialogue if re.search('[a-zA-Z]', x) == None]

# Write to the output file
output_file = open("episode 1/dialogue.txt", "w")
output_file.write('\n'.join(dialogue_no_english))
output_file.close()

print("Transcript Parsed")