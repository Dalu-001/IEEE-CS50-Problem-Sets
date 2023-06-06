#prompt the user for an input
text = input ("Enter a text in camel case: ")

#cher for an upper case letter and replace with an underscore and the lower case of that letter
for char in text:
    if char.isupper():
        char = char.replace(char, "_"+char.lower())

#print out the result
    print (char, end="")