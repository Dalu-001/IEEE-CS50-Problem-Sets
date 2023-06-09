# Felipe's Taqueria

In this code, I created a menu. This menu is a dictionary containing some keys (food items) and their lists (prices of the food items).

I assigned 0.00 to "total", i.e., I set the initial price to 0.00 because no order had been made yet.

Then in a While loop, I used the "try-except" statement.

In this statement, I prompted the user to input an item, I assigned the user's input to the variable "item", then I formatted it so that the initial letter of each string is in upper case since that is how they appeared in the dictionary "menu".

If the item the user inputted is found in menu, the code accesses the list to that key, which is the price of that particular food item.

It then adds that price to the "total" which has an initial value of zero.

It assigns the result to "total" again.

Now "total" is no longer zero. it now has the value of the price of the food item.

This new value of "total" is now printed out.

The user is prompted for another input, and the code repeats the same process again; adding the price of the inputted food item to "total" and printing the new result out.

If the user enters another string that is not in the dictionary, "menu" an error prompt, "invalid" is printed out.

And the user is prompted for another input.

This loop keeps repeating until the user presses control-d which catches the "EOFError" from the "try-except" statement and breaks the loop.
