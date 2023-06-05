while True:
    try:
        x, y = input("Input a fraction: ").split("/")
        x = int(x)
        y = int(y)
        z = x/y

    except ValueError:
        print("Your values must be integers")

    except ZeroDivisionError:
        print("Cannot be divided by zero")

    else:
        if x > y:
            print("x must be less than y")
            continue
        else:
            break

rounded_num = round(z*100)
if rounded_num <= 1:
    print('E')
elif rounded_num >= 99:
    print('F')
else:
    print (f"{rounded_num}%")