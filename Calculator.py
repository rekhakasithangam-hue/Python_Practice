calculate = "Y"
while calculate == "Y":
    a = int(input("Num 1:"))
    b = int(input("Num 2:"))
    c = int(input("Please Enter The 1.+ 2.- 3.* 4./"))
   
    if c == 1:
        print(f"{a}+{b}={a+b}")
    elif c == 2:
        print(f"{a}-{b}={a-b}")   
    elif c == 3:
        print(f"{a}*{b}={a*b}")
    elif c == 4:
        if b==0:
            print("ZeroDivisionError")
        else:
            (f"{a}/{b}={a/b}")
    else:
        print("Check your Number")   
    calculate = input("Continue: Y/N")


print("Thank you for using the calculator!")