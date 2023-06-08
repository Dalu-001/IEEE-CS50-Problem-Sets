# Fuel Gauge
 
 In a loop, the user is prompted to enter a fraction in the format "x/y"
 
 The code performs division for this input (i.e., it divides x by y), and assigns it to the variable 'z'.
 
 Then a couple of errors are checked for corner cases of the input the user may enter
 
 If the code encounters any error, some exceptional statements are made using the try-except statement.
 
 If the user enters a string instead of an integer, it encounters a value error and the warning prompt, "Your values must be integers" is printed. And the user is prompted for an input again
 
 If in the fraction, the user enters zero as the denominator, it encounters a zero-division error, and the warning prompt, "Cannot be divided by zero" is printed. And the user is prompted for an input again.
 
Since we are dealing with percentages, if the numerator is greater than the denominator, a warning prompt, "x must be less than y" is printed out. And the user is prompted for an input again.

If none of these errors are encountered, the loop is broken and the next lines of codes are executed.

'z', which is the result of the division of x and y is rounded up to the nearest integer.

if this rounded up value is less than or equal to 1, 'E' is printed out to indicate Empty.

If the rounded up value is greater than or equal to 99, 'F' is printed out to indicate Full.

