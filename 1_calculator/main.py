while True:
    try:
        a = int(input("\nEnter the number : "))
        b = int(input("Enter the number : "))

        operation = int(input("Enter the operation number\n1:Addition,\n2:substraction,\n3:Multiplication,\n4:Division,\n5:Floor_division,\n6:Modulas\n"))

        match operation:
            case 1:Addition = print(f"{a} + {b} = {a+b}\n")

            case 2:Substraction = print(f"{a} - {b} = {a-b}\n")

            case 3:Multiplication = print(f"{a} X {b} = {a*b}\n")

            case 4:Division = print(f"{a} / {b} = {a/b}\n")

            case 5:Floor_division = print(f"{a} // {b} = {a//b}\n")

            case 6:Modulas = print(f"{a} % {b} = {a%b}\n")
            
            case _: print("invalid operation input")
    except:
        print("Invalid input")
        
    f = int(input("Enter 0 for exit\nEnter any number to continue: "))
    if f == 0:
        break