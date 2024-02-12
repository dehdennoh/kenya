temperature = 34
if temperature > 32:
    print("It is hot")
else:
    print("It is cold")

# A programm that determines largrst number between three
num1 = 43
num2 = 65
num3 = 57

if num1 > num2 and num1 > num3:
    print(num1, "is the largest number")
elif num2 > num1 and num2 > num3:
    print(num2, "is the largest number")
else:
    print(num3, "is the largest number")

# A program that checks whether a number is even or odd
number = 34

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")

# Prime number


num = 80
# If given number is greater than 1
if num > 1:
    # Iterate from 2 to n / 2
    for i in range(2, int(num/2)+1):
        # If num is divisible by any number between
        # 2 and n / 2, it is not prime
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")


num = int(input("Enter a number :"))
if num<=1 :
    print (num, "is not a prime number")
else:
     for i in range(2,num):
       if num % i == 0:
        print(num,"Notprime")
        break
     else:
         print("is a prime number")








