# 5 у вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений.

# file = open('text.txt').read()  # alwayt close file if you don't use context manager
# text = (file .replace('. ', '.\n')).strip()
# sentences = text.split('\n')
#
# for sentence in sentences:
#     print(sentence)
#     print()

# It is dirty hack but it is works =)
# Take a look how it could be solved with regular expression
import re

with open("text.txt") as file:
    text = file.read()

for sentence in re.findall(r"\S.*?[.!?](?=\s|$)", text):
    print(sentence)
    print()
