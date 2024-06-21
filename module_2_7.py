def print_params(a=1, b='строка',c=True):
    print(a,b,c)

values_list = [12345, 'abcdefg', True]
values_dict = {'a': 'Whatsa','b': False, 'c': 00000}
values_list_2 = [1-5, False]

print_params(*values_list)
print_params(**values_dict)
print_params(*values_list_2, 42)
