
# a=1
# b=100
# for i in range(a,b+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)


# def get_same_strings(first_string,second_string):
#     count=[]
#     for i in range (len(first_string)):
#         first_1=first_string[i:]
#         count+=[first_1]
#     for j in range (len(second_string)):
#         second_1=second_string[:j]
#         count+=[second_1]
#     return count
        
        
# first_string=input()
# second_string=input()
# result=get_same_strings(first_string,second_string)
# print(result)
# for i in result:
#     count=result.count(i)
#     if count==2:
#         print(i)
#         break
# else:
#     print("No overlapping")
    

m="maheshsannaila"
# print(m[4:-1])

# print(m[-4:-1])

# print(m[4:-1:1])

# print(m[4:-1:-1])

# print(m[-1:1])

# print(m[-1:1:-1])

# print(m[-3:-6])

# print(m[-3:-6:-1])

# a1=10
# print(type(a1))
# print(float(a1))
# print(str(a1))

# print(bool(a1))
# print(complex(a1))

# a2="mahesh"
# print(int(a2))
# print(type(a1))
# print(float(a2))
# print(str(a2))
# print(complex(a2))
# print(bool(a2))

# a3=3.5
# print(type(a3))
# print(float(a3))
# print(str(a3))
# print(complex(a3))
# print(bool(a3))
# print(int(a3))

# a4=True
# print(type(a4))
# print(int(a4))
# print(float(a4))
# print(str(a4))
# print(complex(a4))
# print(bool(a4))

# a5=complex(10)
# print(int(a5))
# print(type(a5))
# print(float(a5))
# print(str(a5))
# print(complex(a5))
# print(bool(a5))

# a=20
# b=14
# print(a&b)
# print(a|b)
# print(~b)
# print(a^b)
# print(a>>1)
# print(a<<1)






# operators
#arithmetic operators

# a=int(input())
# b=int(input())

# print(a+b)
# print(a-b)
# print(a*b)
# print(a**b)
# print(a/b)
# print(a//b)
# print(a%b)

# relation operators

# print(a>b)
# print(a<b)
# print(a>=b)
# print(a<=b)
# print(a==b)
# print(a!=b)

# logical operators


# x=a>b
# y=a<b
# print(x and y)
# print(x or y)
# print(not(x and y))

# Assignment operators

# m=3
# n=6
# m+=7
# print(m)
# m-=2
# print(m)
# m*=3
# print(m)
# m=24
# m%=3
# print(m)
# m=23
# m/=3
# print(m)
# m//=1
# print(m)
#eval function

# a="10+30+60"
# b="mahesh+sannayila"
# c="3.5+6.5"
# print(eval(a))
# print(eval(b))
# print(eval(c))

# output statements
# m="hi"
# n="iam good in"
# p="python"
# print(m,"\n"+n+p)
# print(m+n," \n"+p)

# print(m,"\t"+n+p)
# print(m+n,"\t"+p)
# print(m,n,p)
# print(m,end=" ")
# print(n,end=" ")
# print(p)
# m=10
# n=20
# p=30
# print(m,"\n",n,p)
# print(m,"\t",n,p)
# print(m,end=" ")
# print(n,end=" ")
# print(p)

# a=int(input())
# b=input()
# print(a+b)
# print(a*b)
# print((b+"\n")*a)

# a=input()
# b=input()
# print(a+b)
# print(a*b)


#conditions
# a = int(input())
# b = int(input())
# if b > a:
#   print("b is greater than a")

# m=int(input())
# if 35<= m <=100:
#     print("Pass")
# elif m>100:
#     print("Invalid Marks")
# else:
#     print("Fail")


# a=["mahesh","suresh","venu","ajay","srinadh"]
# b=input()
# if b in a:
#     print(True)
# else:
#     print(False)
    

# a=int(input())
# if a%2==0:
#     print(a,"is even number")
# else:
#     print(a,"is odd number")



# #leap year

# l=int(input())
# if l%400==0:
#     print(l,"is a leap year")
# elif l%4==0 and l%100!=0:
#     print(l,"is a leap year")
# else:
#     print(l,"is not a leap year")


# a=int(input())
# b=int(input())
# c=int(input())

# if a>b and a>c:
#     print("a is bigger")
# elif b>c and b>a:
#     print("b is bigger")
# else:
#     print("c is bigger")



# # checking given age elgible or not 
# age=int(input())
# if age>=18:
#     print("he is elgible for vote")
# else:
#     print("he is not elgible for vote")


# #check given number positive or negitive
# given_num=int(input())
# if given_num>=0:
#     print(given_num,"is positive number")
# else:
#     print(given_num,"is negitive number")


# a=int(input())
# b=int(input())
# c=(a==b)
# if c:
#     print("square")
# else:
#     print("not a square")



# given_range=int(input())
# for i in range(1,given_range+1):
#     if i%2==0:
#         print("{0} is even".format(i))
#     else:
#         print("{}is odd".format(i))   


# a=input()
# for i in range(5):
#     print(a)

# a=input()
# b=int(input())
# length=len(a)
# n=b%length
# print(n)
# first_string=a[n:]
# second_string=a[:n]
# print(first_string+second_string)

a=int(input())
# #rightangle triangle
# for i in range(1,a+1):
#     print("* "*i)

# #leftangle triangle
# for i in range(1,a+1):
#     left_space=" "*(a-i)
#     print(left_space+left_space+"* "*i)

# #triangle
# for i in range(1,a+1):
#     left_space=" "*(a-i)
#     print(left_space+"* "*i)


# #left+rightangle triangles
# for i in range(1,a+1):
#     left_space="  "*(a-i)
#     print("* "*i+left_space+left_space+"* "*i)

# #diamond shape
# for i in range(1,a+1):
#   left_space=" "*(a-i) 
#   print(left_space+"* "*i)
# for j in range(1,a):
#   left_space=" "*j
#   print(left_space+"* "*(a-j))


#num pattren

#leftangle triangle
# for i in range(1,a+1):
#     print((str(i)+" ")*i)


# for i in range(1,a+1):
#     pattren=""
#     for j in range(1,i+1):
#         # print(str(j),sep=" ")
#         pattren+=str(j)
#     print(pattren)
        