# def get_sum(a):
#     each_num=a[0]
#     if len(a)==1:
#         return each_num
    
#     return (each_num+get_sum(a[1:]))
# a=[3,4,5,5]
# print(get_sum(a))


# def get_factorial(a):
#     if a<0:
#         return 0

#     return a+get_factorial(a-1)

# a=int(input())
# b=get_factorial(a)
# print(b)



# def get_sum_of_square(a):
#     each_num=a[0]**2
#     if len(a)==1:
#         return each_num
#     return (each_num+get_sum_of_square(a[1:]))

# a=[3,4,5]
# print(get_sum_of_square(a))



# get_sum=lambda a,b:a+b
# print(get_sum(10,20))


# def get_sum(m):
#     return lambda n:m+n
# r=get_sum(3)
# print(r(5))

# def check_odd(n):
#     if n%2 !=0:
#         return True
#     else:
#         return False
# list_1=[1,3,4,5,6,7,8,9,12,3,45]
# odd_nums=filter(check_odd,list_1)
# print(list(odd_nums))

def check_odd(n):
    for i in range(2,n):
        if n%i==0:
            break
        else:
            return True
list_1=[1,2,3,4,5,6,7,8,9,10,23,45,6,7,13]
prime_nums= filter(check_odd,list_1)
print(list(prime_nums))