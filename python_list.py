# list comprehension example
list2 = ['codes'*i for i in range(5) if i % 2 ==0]
list1 = ['coder'*i for i in range(5) if i % 2 ==0]
list3 = ['code___'*i for i in range(5) if i % 2 ==0]

print(list1, list2, list3)