text = input ("Input a text: ").lower()
for char in text:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
        char = char.replace(char, "")
        print (char, end="")
    else:
        print (char, end="")