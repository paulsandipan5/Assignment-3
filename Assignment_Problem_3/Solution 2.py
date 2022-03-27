# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def uplow_count():
    s = input()
    count1 = 0
    count2 = 0
    for i in s:
        if i == i.upper() and i!=" ":
            count1+=1
        elif i == i.lower() and i!=' ':
            count2+=1
    return f"No of upper case characters: {count1} No of lower case characters: {count2}"
    
    # call uplow_count()
    # then enter the string
