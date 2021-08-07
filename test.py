import copy
a = [[1, 2, 3], [4, 5, 6]]
copy1 = copy.deepcopy(a)
copy1.append(1)
print(copy1, a)
