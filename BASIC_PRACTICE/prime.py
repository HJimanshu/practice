#wrute a program to given number is prime or not
# num= int(input("Enter any number:"))
# prime=False
# if num>1:
#     for i in range(2,num):
#        if num%i == 0:
#           prime=True
#           break
#     if prime:
#        print(num,"Is not prime")
#     else:
#         print(num,"Is prime")       
    
   
#start astric star pattern
# 1.star pathern
# for i in range(1,5):
#     for j in range(1,5):
#         print("*",end='')
#     print()    
    
#2 star pattern
# for i in range(1,6):
#     for j in range(1,6):
#         if j<=i:
#             print("* ",end='')
#         else:
#             print("-",end='')    
#     print()

#3 star pattern
# for i in range(0,5):
#     for j in range(0,6):
#         if j>=5-i:
#             print("*",end='')
#         else:
#             print(" ",end='')    
        
#     print()  


#4 star pattern
for i in range(1,6):
    for j in range(1,6):
        if j<=6-i:  
            print("*",end='')
        else:
            print(" ",end='')
    print()                 
    
# 5 star pattern
for i in range(0,5):
    for j in range(0,5):
        if j>=i:
            print("*",end='')
        else:
            print(" ",end='')
    print()             
    
    
    
a="blue is sky"
b=a.split()
c=b[::-1]
print(' '.join(c))


#factorial of given number
def factorial(n):
   if n==1:
       return 1
   else:
       return n* factorial(n-1)
num=int(input("Enter the number:"))
print("factorial of given number",num,factorial(num))    