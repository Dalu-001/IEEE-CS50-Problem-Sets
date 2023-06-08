# Coke Machine

In this code, I set the fixed amount of the money the user will spend to be equal to 50. 

Then I prompted the user to for an input, which is the amount the user wishes to spend. (Line 4 "while fix > 0"). So, this loop will continue running so long as fix is greater than zero.

But the user has to input either 5 cents, 10 cents or 25 cents.

If the user inputs anything other than these, he/she is prompted again to enter the amount due.  (Line 9, "While True:")

This keeps happening until the user enters the correct amount. When the user inputs the right amount, the loop breaks. (Line 13 and 14, else: break).

When the user enters a correct amount, it is obviously less than the fixed amount, so the amount the user enters is subtracted from the fixed amount (line 16).

The user is still prompted to enter another amount again, and the same process in 13 above happens. This keeps happening, and the fixed amount keeps reducing until the it is exhausted. And when the user inputs an amount this time, it will be greater than the fixed amount.

A change will be owed, which will be printed out (line 18 - 21).

And the while loop is broken.

