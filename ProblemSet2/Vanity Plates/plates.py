def main():
    #request an input
    plate = input("Plate: ")

#if all the values in the "is_valid" function are met, print out "valid"
    if is_valid(plate):
        print("Valid")

#if they are not met, print out "invalid"
    else:
        print("Invalid")


def is_valid(s):
    length = len(s)

#check for the length of the string
    if length < 2 or length >= 6:
        return False
    
#check if the first 2 characters are alphabets
    if not s[0:2].isalpha():
        return False
    
#check so that if the code encounters the first non-zero number, the remaining characters must be numbers
#if it encounters an alphabet, return false
    for i in range(length):
        if s[i].isnumeric():
            if s[i] == '0':
                return False
            
            for j in range(i+1, length):
                if s[j].isalpha():
                    return False
                break

#check for any space, period or punctuation mark inputted and return false
        if not s.isalnum():
            return False
        
#if all these conditions are met, return true to the function
    return True
                
#call main to make sure the function is ran
main()

    
    