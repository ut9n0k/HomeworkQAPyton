# 1. Написать функцию arithmetic, принимающую 3 аргумента: первые 2 - числа, третий - операция,
# которая должна быть произведена над ними. Если третий аргумент +, сложить их; если —, то вычесть; * — умножить;
# / — разделить (первое на второе). В остальных случаях вернуть строку Not known operation: {operation}.
# Описать функцию в приложенном файле таким образом что бы все проверки в __main__ блоке task_1 выполнялись корректно.
# НЕ НУЖНО ВЫЗЫВАТЬ ФУНКЦИЮ САМИМ Я ЭТО УЖЕ СДЕЛАЛ В УТВЕРЖДЕНИЯХ "assert".

def arithmetic(a, b, operation):

    if operation == "+":
        return a + b
    elif operation == "-":
        return a - b
    elif operation == "*":
        return a * b
    elif operation == "/":
        return a / b
    else:
        print(f"Not known operation: {operation}")


print(arithmetic(7, 7, "+"))