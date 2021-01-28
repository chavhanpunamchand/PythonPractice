# Program to check if a number is prime or not


num1 = 11

# To take input from the user
# num1 = int(input("Enter a number: "))

# prime numbers are greater than 1
if num1 > 1:
    # check for factors
    for i in range(2, num1):
        if (num1 % i) == 0:
            print(num1, "is not a prime number")
            print(i, "times", num1 // i, "is", num1)
            break
    else:
        print(num1, "is a prime number")

# if input number is less than
# or equal to 1, it is not prime
else:
    print(num1, "is not a prime number")
