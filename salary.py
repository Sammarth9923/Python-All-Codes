salary = int(input("enter the salary amount : "))
if salary < 250000:
    print("tax = NIL")
elif 250000 <= salary <= 500000:
    print("tax = 10%")
elif salary>500000:
    print("tax = 20%")


