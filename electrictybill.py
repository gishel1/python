units = int(input("enter the amount of units consumed"))
if units <= 50:
    amount = units * 2.60
    surcharge = 25
elif units <= 100:
    amount = units * 3.25
    surcharge = 35
elif units <=200:
    amount = units * 5.26
    surcharge = 45
else:
    amount = units * 8.45
    surcharge = 75
bill = amount + surcharge
print ("your electricty bill is ", bill)