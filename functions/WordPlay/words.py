import scrabble


print("#" * 10 +  "Print all letters that never appear doubled in englis" + "#" * 10)

letters = 'abcdefghijklmnopqrstuvwxyz'

def has_a_double(letter):
    for word in scrabble.wordlist:
        if letter + letter in word:
            return True
    return False

for letter in letters:
    if not has_a_double(letter):
        print(letter + " never appears doubled")


print("#" * 10 + "Print all words containing 'uu'." + "#" * 10)
for word in scrabble.wordlist:
    if 'q' in word and not 'u' in word:
        print(word)

print("#" * 10 + "Print all words containing all vowels" + "#" * 10)
vowels = 'aeiou'

def has_all_vowels(word):
    for vowel in vowels:
        if vowel not in word:
            return False
    return True
counter = 0
for word in scrabble.wordlist:
    if has_all_vowels(word):
        counter = counter + 1
        print(word)
print(counter)
