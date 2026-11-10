# [] create poem mixer function, call the function with the provided test string
# [] test string: `Little fly, Thy summer’s play My thoughtless hand Has brushed away. Am not I A fly like thee? Or art not thou A man like me?`  
def word_mixer(word_list):
    word_list.sort()
    new_words = []
    while len(word_list) > 5:
        new_words.append(word_list.pop(-5))
        new_words.append(word_list.pop(0))
        new_words.append(word_list.pop())
        new_words.append("\n")
    return new_words
    
string_input = input("Welcome Michelle Liu, enter a poem, verse, or saying: ")
word_list = string_input.split()
length = len(word_list)

for word in range(length):
    if len(word_list[word]) <= 3:
        word_list[word] = word_list[word].lower()
    elif len(word_list[word]) >= 7:
        word_list[word] = word_list[word].upper()
    else:
        pass

mixed_words = word_mixer(word_list)
print(" ".join(mixed_words))