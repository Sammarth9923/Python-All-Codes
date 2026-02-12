cost = int (input("enter the cost price :"))
sell = int (input("enter the selling price :"))
if cost < sell:
    print("user got profit")
elif cost > sell: 
    print("user got loss")
elif cost == sell:
    print("use got no loss no profit")
