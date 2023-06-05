text = input ("Enter a text in camel case: ")
for char in text:
    if char.isupper():
        char = char.replace(char, "_"+char.lower())
    print (char, end="")