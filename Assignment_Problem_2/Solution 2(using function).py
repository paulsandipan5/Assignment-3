# Write a Python program to reverse a string(using function)

def rev_string(s):
    l = len(s)-1
    s1 = ""
    for i in s:
        s1 += s[l]
        l -= 1
    return s1

# rev_string('Edyoda') as input
# 'adoydE' as output