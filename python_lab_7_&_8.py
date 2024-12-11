#7 Uppercase and Lowercase
def count_let(string):
    ucase=0
    lcase=0
    for char in string:
        if char.isupper():
            ucase+=1
        elif char.islower():
            lcase+=1
    return ucase,lcase
string=input()
u,l=count_let(string)
print("Upper case",u)
print("Lower case",l)

#8 Palindrome or not
s=input()
ns=s[::-1]
if s==ns:
    print("Palindrome")
else:
    print("Not a Palindrome")
    
