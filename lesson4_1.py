try:
    print("Start code")
    print(10/0)
    print("No Error")
except (NameError, ZeroDivisionError):
    print("We have an error")



print("code after capsule")