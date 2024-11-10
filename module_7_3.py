class WordsFinder:
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        for_to_replace = ''
        with open(self.file_names, encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                to_replace = [',', '.', '=', '!', '?', ';', ':', ' - ']
                for char in line:
                    if char in to_replace:
                        line = line.replace(char, '')
                for_to_replace += line
            all_words[self.file_names] = for_to_replace.split()

        return all_words

    def find(self, word):
        dictionary_1 = {}
        for i in range(len(self.get_all_words()[self.file_names])):
            if word.lower() == self.get_all_words()[self.file_names][i]:
                dictionary_1[self.file_names] = i + 1
                return dictionary_1

    def count(self, word):
        dictionary_2 = {}
        words = self.get_all_words()[self.file_names]
        dictionary_2[self.file_names] = words.count(word.lower())
        return dictionary_2


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
