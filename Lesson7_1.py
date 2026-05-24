my_list = [1, 2, 3]
interior = iter(my_list)
#print(iterator)

print(next(interior)) # 1
print(next(interior)) # 2
print(next(interior)) # 3
print(next(interior)) # error