#  palindrome
a=input()
revers_a=a[::-1]
if a==revers_a:
    print(a,"is palindrpme")
else:
    print(a,"is not palindrome")

#  vowel or consonent
a=input()
if a=="a" or a=="e" or a=="i" or a=="o" or a=="u":
    print("vowel")
else:
    print("consonent")

#  replace string
a=input()
print(a.replace(" ","-"))

#  remove charecter in string
a=input()
for i in a:
    if i.isalpha():
        r=(a.replace(i,""))
        a=r
print(a)

# checking alphabets integters alphabets
string_a=input()
alphabets=0
integers=0
sp_charecters=0
for i in string_a:
    if i.isalpha():
        alphabets+=1
    elif i.isdigit():
        integers+=1
    else:
        sp_charecters+=1
print(alphabets)
print(integers)
print(sp_charecters)      

remove spaces
a=input()
print(a.replace(" ",""))

# Write a python program to find sum of integers in the string.
a=input()
count=0
for i in a:
    if i.isdigit():
        count+=int(i)
print(count)

# Write a python program to Remov e Repeated Character from String.
a="mahesh"

for i in a:
    c=a.count(i)
    if c>1:
       remove_s =a.replace(i,"")
       remove_s+=i
print(remove_s)



# .Write a Program to Sort the Characters of the String and First Alphabet Symbols followed by Numeric Values.

a="mahesh"
sorted_s=sorted(a)
sorted_string=""
for i in sorted_s:
    sorted_string+=i
print(sorted_string)

# Write a python program to check string is anagrams or not in Python.
a=input()
b=input()
if sorted(a)==sorted(b):
    print("anagram sstrings")
else:
    print("not anagram strigs")

#completed 