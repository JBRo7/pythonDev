#map, filter, zip, and reduce
"""my_list = [1,2,3]
def multiply_by2(item):
    return item*2
#new_list = []
   # for item in li:
        #new_list.append(item*2)
    #return new_list
print(list(map(multiply_by2, my_list)))
print(my_list)
"""

"""#zip
my_list = [1,2,3]
your_list = [10,20,33]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

print("Odd:", list(zip(my_list, your_list)))
print("Original List:", my_list)"""


#lambda expressions
from functools import reduce
my_list = [1,2,3]

def only_odd(item):
    return item % 2 != 0

def accumulator(acc, item):
    print(acc, item)
    return acc + item

#lambda param: action(param), this will automatically return
print("Multiply by 2:", list(map(lambda item: item*2, my_list)))
print("Odd:", list(filter(lambda item: item % 2 != 0, my_list)))
print("Add all the Items:", reduce(lambda acc, item: acc+item, my_list))
print("Original List:", my_list)