# Write a Python program to reverse a string.

string = input()
l = len(string)-1
s1 = ""
for i in string:
    s1 += string[l]
    l -= 1
print(s1)