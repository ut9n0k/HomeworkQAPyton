# У вас есть группа гостей для вип ложи. Места в вип ложе все заняты этими гостями.
# Есть группа гостей в общем зале и места в нем все еще есть. Отобразите 2 группы гостей в коде.

vip = {
    1: 'Vitya Kitsya',
    2: 'Galya Smit',
    3: 'Pesto Pasto',
    4: 'Ivan Banan',
    5: 'Marta Sparta'
}
bastards = {
    1: 'Lily Lolly',
    2: 'Harry Ivi',
    3: None,
    4: 'Ivan Banan',
    5: None
}

print(vip, bastards)

# Good but in my opinion it is over engineered.
# And in this case I suppose vip quests can be increased.
# You should be shure that vip guests will never increased if someonve will try to increase them.
# you can create simple tuple and be sure that this group is static
# vip_quests = ("Jake Mann", "Lisa Blum", "Rick Snow")
# If you want to set some number for guest you should use tuple of tuples
# vip_guests = ((1, "Jake Mann"), (2, "Lisa Blum"), (3, "Rick Snow"))
