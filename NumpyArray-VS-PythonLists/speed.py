# Numpy array vs Python lists

# python's lists
list1 = [i for i in range(10000000)]
list2 = [i for i in range(10000000,20000000)]

list3 = []

for i in range(len(list1)):
    list3.append(list1[i] + list2[i])
