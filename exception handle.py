x = int(input("enter a number: "))
y = int(input("enter a number: "))
z = None
try:
    z = x/y

except Exception as v:
    print("exception type is :",type(v).__name__)

print("the answer is: ",z)