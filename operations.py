import random
import math
print("Random fun calculator")
lucky_number = random.randint(1,100)
print("yourlucky number is" , lucky_number)

activities =[
    "play football" ,
    "swim in swimming pool" ,
    "draw a picture" ,
    "read a book" ,
    "try coding"
]

activity = random.choice(activities)
print("Todays activity is" , activity)

print("Number Guessing Game")
secret_num = random.randint(1,10)

guess = int(input("Guess a number between 1-10"))

if guess == secret_num:
    print("you guessed correctly")
else:
    print("wrong! The number is" , secret_num)

print("math functions")

num = 4.67

print("round up" , num , "=" ,math.ceil(num))
print("round down" , num , "=" , math.floor(num))
print("fabs" , num ,"=" , math.fabs(-15))
print("copysign" , num ,"=" , math.copysign(5 , -2))
print("gcd" ,num , "=" , math.gcd(12,18))