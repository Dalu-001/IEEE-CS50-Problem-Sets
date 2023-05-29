# Meal 

In this program, the user is prompted to write what time it is.

a function, "Convert" is defined which is used to convert this time from the format we all know (hour : minute) to a floating number format (hour.minute).

this new format is returned to the function.

the function with the value returned to it is assigned to the variable, "meal_time".

if-else conditions are then used to check the time the user inputed and print out what meal of the day the user is supposed to take.

if it ranges from 7:00 to 8:00 i.e., 7.0 to 8.0, the program prints out "breakfast".

"7:00 to 8:00" is the normal time format. "7.0 to 8.0" is the floating point format which will help the program compare a range of values effectively.

if it ranges from 12:00 to 13:00 i.e., 12.0 to 13.0, the program prints out "lunch".

"12:00 to 13:00" is the normal time format. "12.0 to 13.0" is the floating point format which will help the program compare a range of values effectively.

if it ranges from 18:00 to 19:00 i.e., 18.0 to 19.0, the program prints out "dinner".

"18:00 to 19:00" is the normal time format. "18.0 to 19.0" is the floating point format which will help the program compare a range of values effectively.

If the user prints any time other than the time required, the program prints out an error message "input a correct time."

The
"if __name__ == "__main__":
    main():"
is used to specify a block of code that will only execute when the module is run as the main program. This is commonly used to define a main function or to execute some specific code when the module is run directly. If the code is imported into another program, the if condition is not satisfied, and the main() function will not be called automatically.
