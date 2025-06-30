originalamount = float(input("enter the original value of the product"))
saleamount = float(input("enter the sale value of the product"))
if( originalamount < saleamount):
    profit = saleamount - originalamount
    print("the profit made was{0}".format(profit))
else:
    print("no profit was made")