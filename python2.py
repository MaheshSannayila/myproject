# # check prime numbers prime num 1 to n
# m=int(input())

# n=int(input())

# for i in range(m,n+1):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)

# # checking prime r not
# a=int(input())

# for i in range(2,a):
#     if a%i==0:
#         print("not prime")
#         break
# else:
#     print("prime num")

# #febonocci series
# a=int(input())
# m=0
# n=1
# for i in range(a):
#     print(m)
#     m,n=n,(m+n)



# # leftangle triangle
# a=int(input())
# for i in range(1,a+1):
#     right_space=" "*(a-i)
#     print(("* "*i)+right_space)

# #leftangle triangle with num
# a=int(input())
# for i in range(1,a+1):
#     for j in range(1,i+1):
#         print(j, end=" ")
#     print("")

#  factorial of n wuth recursion

# def factorial(n):
#     if n==1:
#         return 1
#     return n *factorial(n-1)
# n=int(input())
# print(factorial(n))

# # get_largest_sum_in orderd list
# a=[1,3,-5,4,6,7,-8]
# all_sub_lists=[]
# for i in range(len(a)):
#     for j in range(i+1,len(a)+1):
#         all_sub_lists.append(a[i:j])
# # print(all_sub_lists)
# sum_list=[]
# for i in all_sub_lists:
#     sum_list.append(sum(i))
# for j in (all_sub_lists):
#     if sum(j)== max(sum_list):
#         print(j)

# # print dimond pattren with stars
# a=int(input())
# for i in range(1,a+1):
#     left_space=" "*(a-i)
#     print(left_space+"* "*i)
# for j in range(1,a):
#     left_space= " "*j
#     print(left_space+"* "*(a-j))

# print halo dimond with *

a=int(input())

for i in range(1,a+1):
    left_space=" "*(a-i)
    if i==1:
        print((" "* a)+"*"*i)
    elif i==(a):
        print("* "*(i))
    else:
        halo_space=" "*(2*i-1)
        print(left_space+"*"+halo_space+"* ")







        

        
    
