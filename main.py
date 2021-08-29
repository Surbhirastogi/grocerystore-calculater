sum=0
while(True):
    userinput=input("enter the item price or press q to quit:\n")
    if(userinput!="q"):
        sum=sum+int(userinput)
        print(f"order sum so far: {sum}")

    else:
        print(f" your total bill is worth {sum}\nthanks for shopping with us ")
        break