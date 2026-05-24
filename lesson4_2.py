try:
    print("Hello")
except:
    print("We have problem in block 1")
else:
    print("No problem block 1")

try:
    print(10/0)
except:
    print("We have problem in block 2")
else:
    print("No problem block 2")

try:
    print(10/3)
except:
    print("We have problem in block 3")
else:
    print("No problem block 3")
