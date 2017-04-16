>>> def sum(numbers):
...     total = 0
...     for number in numbers:
...         total = total + number
...     return total
...
>>> sum([1,2,3,4,5])
15
>>> def starts_with_a_vowel(word):
...     return word[0] in "AEIOU"
...
>>> starts_with_a_vowel("Alice")
True
>>> starts_with_a_vowel("Max")
False
>>> names = ["Alice", "Bob", "Cara", "Dan", "Edith"]
>>> def filte_to_vowel_words(word_list):
...     vowel_words = []
...     for word in word_list:
...         if starts_with_a_vowel(word):
...             vowel_words.append(word)
...     return vowel_words
...
>>> filte_to_vowel_words(names)
['Alice', 'Edith']
>>> v = filte_to_vowel_words(names)
>>> exit()
