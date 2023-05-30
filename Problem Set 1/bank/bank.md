# Bank

In this code, the user is prompted to enter a greeting.

this greeting (which is a string) is formatted so that any upper case letter is changed to lower case, this is because the greeting is case insensitive.

In line 4, the line of code:
"if greet.startswith("hello"):
    print ("$0")
as self-explanatory as it appears, means that if the greeting the user entered starts with "hello", the program should print "$0" on the screen.

the next lines of code (from line 6):
"elif greet.startswith("h"):
    print ("$20")"
means that if instead of "hello" the user enters a greeting that starts with the letter 'h', the program should print out "$20".

Notice the format of precedence that we used. The greeting, "hello" took precedence over a greeting that starts with the letter 'h', because if it had been the other way round, we would not get our desired result.

This is because "hello" itself starts with the letter 'h', so if the if statement involving the letter 'h' had been used first, and the user enters hello, the condition would be true for the first statement and print out $20 instead of $0.

So the if statement with "hello" had to come first, so that the program will carry out the correct condition for the if statement involving "hello" if the user inputs "hello" as a greeting.

And if the user inputs another greeting that begins with the letter 'h', say "hey" for instance, the if statement will not be true, so it will move on to the next line and evaluate the if statement involving 'h', which will be true and $20 will be printed on the screen.

If none of the conditions are met at all (i.e., the user enters a greeting that does not start with "hello" or 'h', then $100 will be printed on the screen.
