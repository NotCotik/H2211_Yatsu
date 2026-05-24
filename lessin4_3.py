def checker(var1):
    if type(var1) != str:
        raise TypeError(f"We are sorry but we work with {type(var1)}, need only str")
    else:
        return var1

f_var = "Vasya"
s_var = 6

checker(f_var)
checker(s_var)