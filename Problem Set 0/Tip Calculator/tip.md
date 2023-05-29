# Tip Calculator

In this program, the main function is defined.

"dollars_to_float" function is called, in which an argument, "dollars" is passed into.

This argument is an input which is the price of a meal, i.e., a floating point number preceded by a dollar sign.

"percent_to_float" function is also called, and an argument, "percent" is also passed into it as well.

This argument is an input which is the percentage of the payment you would like to pay as tip, i.e., a floating point number succeeded by the percentage sign.

tip is calculated, which is the product of dollars and percent.

"dollars_to_float" function is now defined, and what it does is remove the dollar sign from the dollar variable and make it just a floating point number.

I did this using the ".removeprefix()" method which removes whatever string that comes before our main string. This unwanted string is indicated inside the braces.

After this, the new string is converted to a float and this float is returned to the function so that the function can perform as expected when it is called upon

"percent_to_float" function is also defined, and what it does is remove the percentage sign from the percent variable, making it a floating point number.

I did this using the ".removesuffix()" method which removes whatever string that comes after our main string. This unwanted string is indicated inside the braces.

After this, the new string is converted to a float and divided by 100. The resulting value is returned to the function so that the function can perform as expected when it is called upon

After all these, the main function is called, so it carries out the entire code beneath line 1, multiplies dollar (which is now a floating point number) by percent (which is also now a floating point number)

The result is then printed out to two decimal places.
