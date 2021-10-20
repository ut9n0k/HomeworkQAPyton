# 4 у вас есть список имен переменных в формате кэмел кейс ["FirstItem", "FriendsList", "MyTuple"] преобразовать его
# в список имен переменных для пайтона в формате снейк кейс ["first_item", "friends_list", "my_tuple"]

camel = ["FirstItem", "FriendsList", "MyTuple"]
snake = []

for item in camel:
    for letter in item:
        if letter.isupper() and item.index(letter) != 0:
            snake.append(item.replace(letter, '_' + letter).lower())

print(snake)

# Good.