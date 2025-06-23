amount = int(input("enter the value of money"))
 
note1 = amount//100
note2 = (amount%100)//50
note3 = ((amount%100)%50)//10

print("the number of the first notes are",note1)
print("the number of the second notes are",note2)
print("the number of the third notes are", note3)