#prompt the user for an input
text = input ("Input a text: ").lower()

#if it encounters any vowel, remove the vowel
for char in text:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        char = char.replace(char, "")
        print (char, end="")
    else:
        print (char, end="")