# 1.Write a Python script to add a key to a dictionary.
# Sample Dictionary : {0: 10, 1: 20}
# Expected Result : {0: 10, 1: 20, 2: 30}

a={0: 10, 1: 20}
a[2]=30
print(a)


# 2.Write a Python script to check whether a given key already exists in a dictionary.
a={"mahesh":"2","suresh":"5","girish":"35"}
b=input()
keys=list(a)
if b in keys:
    print("alredy exists")
else:
    print("key not in a dictionary")

# 3.Write a Python program to iterate over dictionaries using for loops

a={"mahesh":"2","suresh":"5","girish":"35"}
for i in a.items():
    print(i)

# 4.Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) and the values are the square of the keys.
# Sample Dictionary
dict_a={}
for i in range(1,15+1):
    dict_a[i]=(i**2)
print(dict_a)

# 5.Write a Python program to create a dictionary from a string.
# Expected output: {'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}
string_a="marolix technology"
string_a=string_a.replace(" ","")
conve_list=list(string_a)
reversed_list=conve_list[::-1]
for i in reversed_list:
    if (reversed_list.count(i))>1:
        reversed_list.remove(i)
duplicat_removed_list=reversed_list[::-1]
result={}
for i in duplicat_removed_list:
    count_1=conve_list.count(i)
    result[i]=count_1
print(result)
    
# 6 Write a Python program to sum all the items in a dictionary.
a={'m': 1, 'a': 1, 'o': 3, 'l': 2, 'i': 1, 'x': 1, 't': 1, 'e': 1,'c': 1, 'h': 1, 'n': 1, 'g': 1,'y':1}
len_a=len(a)
print(len_a)

# 7.Write a Python program to combine two dictionary by adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
list_keys=list(d2)
d3={}
for i,j in d1.items():
    if i in list_keys:
        m=d2.get(i)
    else:
        m=0
    d3[i]=m+j
print(d3)

# 8.Write a Python program to access dictionary key's element by index.
# Expected Output:
# physics
# math
# chemistry

# 9.Write a Python program to remove a key from a dictionary

d1 = {'a': 100, 'b': 200, 'c':300}
print(d1.pop("a"))
print(d1)

# 10.Write a Python script to merge two Python dictionaries.d
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'g': 300, 'e': 200, 'd':400}
print(d1|d2)