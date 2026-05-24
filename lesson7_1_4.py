
def raise_to_degrees(number, max_degree):
    i = 1
    for  _ in range(max_degree):
        yield number ** i
        i += 1

res = raise_to_degrees(122, 500)
#print(res)

for el in res:
    print(el)
