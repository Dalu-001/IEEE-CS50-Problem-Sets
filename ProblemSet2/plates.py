def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    num = len(s)
    if num >= 2 and num <= 6:
        i = 2
        j = 2
        for i in range(num):
            if (s[0:i].isalpha() and s[0:i].isupper()):
                for j in range(num):
                    if (s[j:].isdigit() and s[j] != "0"):
                        for k in s:
                            if not k == [" ", ".", ",", "?", "!", ";", ":", '"']:
                                return True
                            else:
                                return False
                        else:
                            return False
            
    
main()