# [] create words after "G" following the Assignment requirements use of functions, methods and keyowrds
# Sample quote: "Wheresoever you go, go with all your heart" ~ Confucius (551 BC - 479 BC)

phrase = input("enter a 1 sentence quote, non-alpha separate words: ")
word = ""

for letter in phrase + " ":
    if letter.isalpha():
        word = word + letter
    else:
        if word != "" and word[0].lower() > "g":
            print(word.upper())
            word = ""
        else:
            word = ""

