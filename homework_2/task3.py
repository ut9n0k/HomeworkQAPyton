# У вас есть 3 группы людей bigno_blacklist, poker_blacklist, majong_blacklist.
# Имена людей в формате "John Dow" первое и второе имя. Найти тех кто состоит во всех черных списках.

bigno_blacklist = {"John Dow", 'Marta Hey', 'Gaga Gaga'}
poker_blacklist = {"John Dow", 'Harry Hai', 'Gugu Gaga'}
majong_blacklist = {"John Dow", 'Hou Hou', 'Gigi Gigi'}
print(bigno_blacklist.intersection(poker_blacklist, majong_blacklist))

# Good
