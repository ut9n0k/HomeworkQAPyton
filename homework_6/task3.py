# 3. Написать функцию is_prime, принимающую 1 аргумент — число от 2 до 1000,
# и возвращающую True, если оно простое, и False - иначе.

def is_prime(a):
    if a < 2 or a > 1000:
        return "Number out of range"
    for number in range(2, a-1):
        if a % number == 0:
            return False
        else:
            return True


print(is_prime(0))
print(is_prime(5))
print(is_prime(6))
print(is_prime(1001))
