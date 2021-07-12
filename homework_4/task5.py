# 5 у вас есть текст разбейте текст по предложениям. В качестве результата вы должны получить список из предложений.

file = open('text.txt').read()
text = (file .replace('. ', '.\n')).strip()
lines = text.split('\n')

print(lines)
