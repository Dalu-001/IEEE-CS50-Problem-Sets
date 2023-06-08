# Vanity Plates
 
 In this code, a main function is defined.
 
 In this main function, the user is prompted to input a series of characters (letters and numbers).
 
 This input is passed into a function called "is_valid()"
 
 In this function, "is_valid()":
 
 The length of the string is assigned to a variable, "length"
 
 The code then checks if the length is a minimum of two and a maximum of six characters.
 
 Then it checks if the first two characters are alphabets.
 
 If they are alphabets, it moves on to the next character.
 
 From the third character, the code goes into a loop (and keeps iterating over the consequent characters) and checks for a number.

Once a number is encountered it checks if a letter will come after that number. If it encounters a letter after the first number, the code breaks, else it keeps on iterating and checking.

It also checks if the first number encountered is a non-zero number. If it is the number is zero, the code breaks.

After that, it checks for white spaces, periods, or punctuation marks. If any of these are encountered, the code breaks.

Now if all of the right conditions are met, the code returns True to the "is_valid()" function that was called in main(). If it meets any false conditions or any condition that causes it to break, it returns False to the "is_valid()" function.

The Main function is now called which now prints "Valid" if True is returned to the "is_valid()" function or "Invalid" if False is returned to the "is_valid()" function.
