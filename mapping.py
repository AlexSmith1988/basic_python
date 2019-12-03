from functools import reduce

inc = lambda x: x + 1
mult2 = lambda x: x * 2

# Default way to map-apply two functions and print result
print(list(map(mult2, map(inc, (1, 2, 3, 4, 5)))))


# More functional-style solution
class Mapper:
    _iterable = None

    def __init__(self, iterable):
        self._iterable = iterable

    def map(self, f): return Mapper(map(f, self._iterable))

    def flatMap(self, f): return Mapper(list(map(f, self._iterable)))

    def reduce(self, f): return reduce(f, self._iterable)

    def foreach(self, f):
        for e in self._iterable:
            f(e)
        return self

    def asList(self): return list(self._iterable)

    def __repr__(self):
        reduced = reduce(lambda x, y: f"{x}, {y}", self._iterable)
        return f"({reduced})"


def mappable(data): return Mapper(data)


mappable(range(5)).map(inc).map(mult2).flatMap(print)
print(mappable(range(5)).map(inc).map(mult2).reduce(lambda x, y: x + y))
