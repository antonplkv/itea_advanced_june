class MyRange:

    def __init__(self, start, end, step=1):
        self._start = start
        self._end = end
        self._step = step

    def __iter__(self):
        return self

    def __next__(self):
        if self._start < self._end:
            value = self._start
            self._start += self._step
            return value
        else:
            raise StopIteration

my_range = MyRange(0, 5)

print(list(my_range))