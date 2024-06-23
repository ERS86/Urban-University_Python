def get_multiplied_digits(number):
    str_number = str(number)
    def multiply_digits(s):
        if not s:  #если строка пуста
            return "Нет числа"
        elif len(s) == 1:  #если в строке одна цифра
            return int(s)
        else:
            return int(s[0]) * multiply_digits(s[1:]) if s[0] != '0' else multiply_digits(s[1:])
    return multiply_digits(str_number)

print(get_multiplied_digits('12345'))   #результат: 120
print(get_multiplied_digits('1012'))    #результат: 2
print(get_multiplied_digits('0'))       #результат: 0
print(get_multiplied_digits('5'))       #результат: 5
print(get_multiplied_digits(''))        #результат: Нет числа
print(get_multiplied_digits('000123'))  #результат: 6
