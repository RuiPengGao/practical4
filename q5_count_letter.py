#count letter
string = input("Enter word/ sentence:")
character = input ("Enter a letter:")

def count_letter(str,ch):
    if len(str) == 0:
        return 0
    return (str[0] == ch) + count_letter(str[1:],ch)

print("number of occurence of letter entered is:",count_letter(string, character))
