from typing import Counter

# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'
# ???
print(Counter(word.lower())['а'])

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
count_consonants=lambda x:sum(map(x.count,'бвгджзйклмнпрстфхцчшщ'))
print(count_consonants(word))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
for word in sentence.split():
    print(word[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
# ???
i = 0
for world_len in sentence.split():
    i += len(world_len)
print(f'Avarage value: {round(i/len(sentence.split()))}')