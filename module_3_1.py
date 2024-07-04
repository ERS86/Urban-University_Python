def single_root_words(root_word, *other_words):
    same_words = []
    root_word_lower = root_word.lower()
    for same in other_words:
        same_lower = same.lower()
        if root_word_lower in same_lower or same_lower in root_word_lower:
            same_words.append(same)
    return same_words


result1 = single_root_words('авто', 'АВТОБИОГРАФИЯ', 'автобус', 'абрикос', 'АВТОГРАФ', 'автократ',
                            'АВТОМАТ', 'автомобиль', 'АВТОР', 'авторитет', 'авария')
result2 = single_root_words('Bab', 'Babbitry', 'babblative', 'babblement', 'babbler', 'bobo', 'BABEL')
print(result1)
print(result2)
