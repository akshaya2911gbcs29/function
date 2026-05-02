def sumdigits(n):
    if n==0:
        return 0
    else:
        return n%10+sumdigits(n//10)
n=int(input("Enter a number:"))
print("Sum of digits:",sumdigits(n))
