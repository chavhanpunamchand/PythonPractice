'''
2.Write a function called fizz_buzz that takes a number.
    1.	If the number is divisible by 3, it should return “Fizz”.
    2.	If it is divisible by 5, it should return “Buzz”.
    3.	If it is divisible by both 3 and 5, it should return “FizzBuzz”.
    4.	Otherwise, it should return the same number.

'''
def fizzBuzz(a):
    if a%3==0 and a%5==0:
        return "FizzBuzz"
    elif a%3==0:
        return "Fizz"
    elif a%5==0:
        return "Buzz"
    else:
        return a

while True:
    a=int(input("Enter the num: "))
    print(fizzBuzz(a))
