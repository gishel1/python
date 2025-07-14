#question1
name = str(input("input your name"))
age = int(input("input your age"))
height = float(input("input your height"))
present = bool(input("are you present??"))

print("the variable type of name is:", type(name))
print("the variable type of age is:", type(age))
print("the variable type of height is:", type(height))
print("the variable type of present is:", type(present))

#question2
num1 = int(input("enter your number"))
remainder = num1 % 2
if remainder == 0:
    print("the number is even")
else:
    print("the number is odd")

#question3
weight = int(input("enter your weight in kg"))
height = int(input("enter your height in cm"))
bmi = (weight/ (height * height))
if bmi <= 18.5:
    print("you are underweight")
elif bmi <= 24.9:
    print("you are normal weight")
elif bmi <= 29.9:
    print("you are overweight")
elif bmi <= 30:
    print("you are obese")
elif bmi <= 34.9:
    print("you are obese in class 1")
elif bmi <= 39.9:
    print("you are obese in class 2")
elif bmi >= 40 :
    print("you are obese in class 3")

#question4
maths = int(input("input your score for maths out of 100"))
english = int(input("input your score for english out of 100"))
science = int(input("input your score for science out of 100"))
history = int(input("input your score for history out of 100"))

averagegrade = ((maths + english + science + history)/4)
print("your average grade is", averagegrade)
if averagegrade >= 90 and averagegrade <= 100:
    print("you got an a on the exam")
elif averagegrade >= 80 and averagegrade <= 90:
    print("you got a b on the exam")
elif averagegrade >= 70 and averagegrade <= 90:
    print("you got a c on the exam")
elif averagegrade >= 60 and averagegrade <= 70:
    print("you got a d on the exam")
elif averagegrade >= 50 and averagegrade <= 60:
    print("you got a f on the exam")
else:
    print("you failed the exam")

#question5
