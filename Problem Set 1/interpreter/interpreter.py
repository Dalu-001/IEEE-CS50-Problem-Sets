x, y, z = input("Input your expression: ").split()
x = float(x)
y = str(y)
z = float(z)

match y:
    case "+":
        print (f"{x+z:.1f}")

    case "-":
        print (f"{x-z:.1f}")

    case "*":
        print (f"{x*z:.1f}")

    case "/":
        print (f"{x/z:.1f}")

    case _:
        print ("Please, input a correct expression")