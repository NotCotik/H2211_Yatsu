
class counter:
    def __init__(self, max_number):
        self.i = 0
        self.max_number = max_number

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        self.i += 1
        if self.i > self.max_number:
            raise StopIteration
        return self.i

count =  counter(5)

print(count.__next__())
print(count.__next__())
print(count.__next__())
print(count.__next__())
print(count.__next__())
