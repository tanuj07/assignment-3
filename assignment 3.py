#Question-1
a=[]
n=int(input("enter size of list"))
for i in range(0,n):
    b=int(input())
    a.append(b)
print(a)

#Question-2
c=["google","apple","facebook","microsoft","tesla"]
a.append(c)
print(a)

#Question-3
a="My name is is Tanuj"
b=input("enter the object")
print(a.count(b))

#Question-4
a=[2,88,55,78,99,3]
a.sort()
print(a)

#Question-5
x=[3,6,8,9,10]
y=[4,7,11,15,16]
z=[]
z=x+y
z.sort()
print(z)

#Question-6
a=[]
even=0
odd=0
n=int(input("Enter size of list"))
for i in range(0,n):
    b=int(input())
    a.append(b)
    if b%2==0:
        even=even+1
    else:
        odd=odd+1
print("list -",a)
print("list contains %d even and %d odd numbers."%(even,odd))

#Question-7
a=[5,6,7,8,9]
b=slice(-1,-6,-1)
print(a[b])

#Question-8
a=[5,6,7,8,9]
print("Largest element of tuple ",max(a))
print("Smallest element of tuple ",min(a))

#Question-9
a="conor mcregor"
print(a.upper())

#Question-10
a="3,4,5,6,7"
if a.isalnum():
    print("true")
else:
    print("false")

#Question-11
a="Floyd Mayweather"
print(a.replace("Floyd","Champ"))
