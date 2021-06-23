# У вас есть 2 компании с людьми. Одна из компаний пусть будет это global_logic была поглощена компанией toshiba.
# Отобразите это в коде. Учитывайте что люди с одинаковыми именами могут быть в обеих компаниях.

global_logic = ['John', 'Vova', 'Sergey', 'Valeriy']
toshiba = ['John', 'Tanya', 'Sergey', 'Vika']
global_logic.extend(toshiba)
print(global_logic)