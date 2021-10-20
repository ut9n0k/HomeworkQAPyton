# 2 есть список друзей ["John", "Marta", "James", "Amanda", "Marianna"]. выведите в консоль имена каждое с новой строки
# выровняв по правой стороне используя метод строки и форматирование через f string.
# Так же над именами первой строкой выведини заговловок Names где слово names должно быть посредине а остальное
# пространство заполнено скажем символом "*"

people = ["John", "Marta", "James", "Amanda", "Marianna"]
print("Names".center(150,'*'))
for name in people:
    print(f"{name.rjust(150)}")

# Good but solved only with rjust. You can make names in the center by fstring and make align of all names right with fstring tooo.
# -2 points
