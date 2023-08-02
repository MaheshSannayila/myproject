
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
        

# membership operator

# a=["mahesh","suresh","ganesh","ramesh"]
# b=input()
# if b in a:
#     print(True)
# else:
#     print(False)

# c=input()
# if c not in a:
#     print(True)
# else:
#     print(False)

#space removing
# a=input()
# print(a)
# print(a.strip())
# print(a.rstrip())
# print(a.lstrip())
# b=input()
# print(a.count(b))
# print(a.find(b))
# print(a.index(b))

# print(a[3:1:1])