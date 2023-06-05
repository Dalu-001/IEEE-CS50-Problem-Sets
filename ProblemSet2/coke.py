fix = int(50)

while fix > 0:
    print ("Amount due:", fix)
    while True:
        coin = int(input ("Insert coin: "))
        if coin != 5 and coin != 10 and coin != 25:
            print("You need to insert either 5, 10 or 25 cents.")
        else:
            break
    if fix > coin:
            fix -= coin
    else:
        coin -= fix
        print ("Change owed:", coin)
        break