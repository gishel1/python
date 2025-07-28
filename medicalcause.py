medcause = input("Do you have a medical cause? Enter 'Y' for yes and 'N' for no.")
if medcause == "N":
    attendance = int(input("enter your attendance"))
    if attendance >= 75:
        print("you are eligible take the exam")
    else:
        print("you are not eligible to take the exam")
else:
    print("you are eligible to take the exam")