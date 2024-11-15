def all_variants(text):
    for i in range(len(text)):
        next_string = i + 1
        x = 0
        while len(text) - x > 0:
            if len(text[x: x + next_string]) == next_string:
                yield text[x: x + next_string]
            x += 1


a = all_variants("abc")
for i in a:
    print(i)
