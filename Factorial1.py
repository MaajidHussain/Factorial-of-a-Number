def Factorial(number):
    return 1 if (number==0 or number ==1) else number*Factorial(number-1)
Number=int(input("Enter any whole number: "))
print(Factorial(Number))