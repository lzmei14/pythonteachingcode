# [ ] create, call and test the str_analysis() function  
def str_analysis(test):
    if test.isdigit():
        number = int(test)
        if number > 99:
            return test + " is a pretty big number"
        else:
            return test + " is a smaller number than expected"
    else:
        if test.isalpha():
            return '"' + test + '" is all alphabetical characters!'
        else:
            return '"' + test + '" is neither all alphabetical or all digits. Hmm...'

user_test = ""
while user_test == "":
     user_test = input("Michelle Liu, enter word or integer: ")
print(str_analysis(user_test))
