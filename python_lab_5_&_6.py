#5factorial using recursion
def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
num=int(input("Enter the number:"))
print(f"The factorial is {factorial(num)}")

#6odd or even
n=int(input("Enter the number of elements:"))
arr=[]
for i in range(n):
    arr.append(int(input("Enter the elements:")))
odd=0
even=0
for i in arr:
    if i%2==0:
        even+=1
    else:
        odd+=1
print("The number of odd numbers is",odd)
print("The number of even numbers is",even)

