
while True:
    a = input("Enter 1 number\n")
    if a.strip():
       print("Success")
    else:
        print("ERROR")




    print("+,-,*,/")
    b = input("Enter sign\n")
    c = float(input("Enter 2 number\n"))
    if b == "+":
        print(a+c)
    elif b == "-":
        print(a-c)
    elif b == "*":
        print(a*c)
    elif b == "/":
        print (a/c)
    else:
       print ("Erorrrrrrrrr")
