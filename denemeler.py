#Write a Python code to find intersection of below lists using Lambda.
list1 = [11, 4, 5, 9, 7]
list2 = [5, 10, 4, 1, 10]
list3 = [7, 3, 9, 5, 1]



print(list(filter(lambda x: x in list2 and x in list3, list1)))