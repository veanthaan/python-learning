age = int(input("Enter your age:"))
if age >=18:
    print("you are eligible for vote")
else:
    print("not eligible")

num = int(input("Enter your number:"))
#odd or even check
if num % 2 ==0:
    print("Even number")
else:
    print("odd number")

#positive/negative check
 
num = int(input("Enter your number:"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")

a = int(input("Enter your number:"))
b = int(input("Enter your number:"))

if a > b:
    print("A is bigger")
else:
    print("B is bigger")

mark = int(input("Enter your mark:"))
if mark > 90:
    print("Excellenr")
elif mark > 50:
    print("pass")
else:
    print("fail")
