"""
Parses html dialogue and outputs as a text file
"""
from bs4 import BeautifulSoup
import re

file = open('episode 1/dialogue_animelon.html', mode='r')
html = file.read()
file.close()

parsed_html = BeautifulSoup(html, 'lxml')
# Each segment of dialogue is store in a history element div
dialogue_history_elements = parsed_html.find_all("div", {"class": "dialogueHistoryElement"})
dialogues = []
for element in dialogue_history_elements:
	text = element.text.split()
	dialogues.append(text)

# Output Non-English words only. English words usually appear in the
# theme song
output_file = open("episode 1/dialogue.txt", "w")
for i, dialogue in enumerate(dialogues):
	for word in dialogue:
		if re.search('[a-zA-Z]', word) == None:
			output_file.write(word + '\n')
output_file.close()

print("Generated dialogue.txt")