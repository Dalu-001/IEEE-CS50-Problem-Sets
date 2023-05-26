def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}") #rounding the result to  to 2 d.p

def dollars_to_float(d):
    d = d.removeprefix('$') #removing the prefix '$' from the string
    return float(d) #converting the string to float and returning it to the function

def percent_to_float(p):
    p = p.removesuffix('%') #removing the suffix '%' from the string
    p = float(p)/100 #converting the string to float and dividing by 100
    return p #returning the result to the function

main()