def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
a=int(input("Enter a number:"))
b=int(input("Enter another number:"))
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
print("5.Exit")
ch=int(input("Enter your choice:"))
if ch==1:
    print("sum:",add(a,b))
elif ch==2:
    print("sub:",sub(a,b))
elif ch==3:
    print("multi:",mul(a,b))
elif ch==4:
    print("divide:",div(a,b))
elif ch==5:
    print("Exit")
    exit()
else:
    print("Invalid input")

