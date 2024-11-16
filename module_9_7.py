def is_prime(func):
    def wrapper(*args):
        a = func(*args)
        b = 0
        for i in range(2, a // 2 + 1):
            if a % i == 0:
                b = b + 1
        if b <= 0:
            print("Простое")
        else:
            print("Составное")
        return a
    return wrapper

@is_prime
def sum_three(*args):
    sum_of_three = 0
    for i in args:
        sum_of_three += i
    return sum_of_three


result = sum_three(2, 3, 6)
print(result)
