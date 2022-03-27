#  Write a Python function to sum all the numbers in a list.

def add_list(*data):
    sum = 0
    for i in data:
        sum+=i
    return str(sum) + " is the total sum of list" 

# call add_list(10,20,30,40)
# output will be 100 like this