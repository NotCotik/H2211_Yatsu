def adder(*args, **kwargs):
    result = 0

    for i in args:
        if type(i) == int or type(i) == bool or type(i) == float:
            result += i
        else:
            try:
                result += float(i)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(i)
                continue
            except (ValueError, TypeError):
                pass
    for i in kwargs.values():

        if type(i) == int or type(i) == bool or type(i) == float:
            result += i
        else:
            try:
                result += float(i)
                continue
            except (ValueError, TypeError):
                pass
            try:
                result += int(i)
                continue
            except (ValueError, TypeError):
                pass

    return result
