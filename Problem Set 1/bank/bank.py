#prompt the user to say a greeting
#convert the greeting to be in all lower case, since it is case insensitive
greet = input ("Input a greeting: ").lower()
if greet.startswith("hello"):
    print ("$0")
elif greet.startswith("h"):
    print ("$20")
else:
    print ("$100")
