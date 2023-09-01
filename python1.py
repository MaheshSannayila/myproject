# count Upper case and lower case
def find_num_of_uppercase_and_lowercase(a):
    upper_count=0
    lower_count=0
    for i in a:
        if i.isupper():
            upper_count+=1
        else:
            lower_count+=1
    print(upper_count)
    print(lower_count)

a=input()
find_num_of_uppercase_and_lowercase(a)

# get a unique list

def get_unique_list(a):
    unique_list=[]
    for i in a:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)

a=[1,2,3,3,3,3,4,5]
get_unique_list(a)

# sum all the numbers in a list.

def get_sum(a):
    sum=0
    for i in a:
        sum+=i
    print(sum)
a=[8, 2, 3, 0, 7]
get_sum(a)

# pangram r not

def find_pangram_r_not(a):
    unique_set=(set(a))
    if len(unique_set)==26:
        print("its pangram")
    else:
        print("not pangram")

a=input()
a=a.replace(" ","")
find_pangram_r_not(a)

# print a list where the values are the squares of numbers between 1 and 10 (both included).

def get_nums_sqrs_list(a,b):
    list_1=[]
    for i in range(a,b):
        list_1.append(i**2)
    print(list_1)
a=int(input())
b=int(input())
get_nums_sqrs_list(a,b+1)

# find sum of given values, pass values has variable number of arguments to function.

def get_sum_args(*a):
    sum=0
    for i in a:
        sum+=i
    print(sum)

get_sum_args(1,2,3,4,5)
