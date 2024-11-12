def add_everything_up(a, b):
    try:
        return round((a + b), 3)
    except TypeError:
        a2 = str(a)
        b2 = str(b)
        return a2 + b2


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
