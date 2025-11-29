# Numpy array vs Python lists

# python's lists
a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []

for i in range(len(a)):
    c.append(a[i] + b[i])
    