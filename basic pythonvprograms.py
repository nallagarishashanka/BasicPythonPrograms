#prime number
n=int(input("enter a number"))
if n>1:
    for i in range(2,n):
        if n%i==0:
            print(n,"not a number")
            break
    else:
        print(n,"is a prime number")

#prime numbers between 1 and 100
lower=1
upper=100
print("the prime numbers between", lower,"and", upper, "are:")
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print(num)

#reverse of a number
n=int(input("enter a number:"))
rev_num=0
while n>0:
    remainder=n%10
    rev_num=(rev_num*10)+remainder
    n=n//10
print("The reverse of a number is:",rev_num)

#armstrong number
n=str(int(input("enter a number:")))
dig_sum=0
for i in n:
    dig_sum=dig_sum+int(i)**len(n)
if(int(n)==dig_sum):
    print("armstrong number")
else:
    print("not a armstrong number")
#factorial of a number
a=int(input("enter a number:"))
factorial=1
if a<0:
    print("factorial does not exist for negative numbers")
elif a==0:
    print("the factorial of 0 is 1")
else:
    for i in range(1,a+1):
        factorial=factorial*i
    print("the factorial of",a,"is",factorial)

#sum of n numbers
n=int(input("enter a limit"))
s=0
for i in range(1,n+1):
    s=s+i
print("the sum is",s)

#multiplication table
a=int(input("enter the multiplication table"))
for i in range(1,11):
    print(a,"X",i,"=",a*i)

#pattern 1,22,333,4444
n=int(input("enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end="")
    print()

#pattern 1,22,33
for i in range(1,10):
    print(str(i) *i)

