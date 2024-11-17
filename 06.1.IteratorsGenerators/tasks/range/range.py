from collections.abc import Iterable, Iterator, Sized


class RangeIterator(Iterator[int]):
    """The iterator class for Range"""
    def __init__(self, range_: 'Range') -> None:
        self.new_one =  range_


    def __iter__(self) -> 'RangeIterator':
        return self

    def __next__(self) -> int:
        self.new_one.current += self.new_one.step
        if ((self.new_one.step > 0 and self.new_one.current < self.new_one.end) or
                (self.new_one.step < 0 and self.new_one.current > self.new_one.end)):
            return self.new_one.current
        else:
            raise StopIteration()


class Range(Sized, Iterable[int]):
    """The range-like type, which represents an immutable sequence of numbers"""

    def __init__(self, *args: int) -> None:
        """
        :param args: either it's a single `stop` argument
            or sequence of `start, stop[, step]` arguments.
        If the `step` argument is omitted, it defaults to 1.
        If the `start` argument is omitted, it defaults to 0.
        If `step` is zero, ValueError is raised.
        """
        self.num_args = len(args)
        if len(args) == 1:
            self.start = 0
            self.end = args[0]
            self.step = 1
        elif len(args) == 2:
            self.start = args[0]
            self.end = args[1]
            self.step = 1
        else:
            self.start = args[0]
            self.end = args[1]
            self.step = args[2]

        if self.step == 0:
            raise ValueError


    def __iter__(self) -> 'RangeIterator':
        self.current = self.start - self.step
        return RangeIterator(self)

    def __repr__(self) -> str:
        if self.step == 1:
            return f'Range({self.start}, {self.end})'
        else:
            return f'Range({self.start}, {self.end}, {self.step})'

    def __str__(self) -> str:
        if self.step == 1:
            return f'range({self.start}, {self.end})'
        else:
            return f'range({self.start}, {self.end}, {self.step})'

    def __contains__(self, key: int) -> bool:
        if self.step > 0:
            if self.start <= key <= self.end:
                if (key - self.start) % self.step == 0:
                    return True
                else:
                    return False
            else:
                return False
        else:
            if self.start >= key >= self.end:
                if (key - self.start) % self.step == 0:
                    return True
                else:
                    return False
            else:
                return False

    def __getitem__(self, key: int) -> int:
        if self.step > 0:
            self.poln = (self.end - self.start) % self.step
            if self.poln == 0:
                self.numofnum = (self.end - self.start) // self.step
            else:
                self.numofnum = (self.end - self.start + self.step - self.poln) // self.step

            if -self.numofnum < key < self.numofnum:
                return self.start + key * self.step
            else:
                raise IndexError
        else:
            self.poln = (-self.end + self.start) % -self.step
            if self.poln == 0:
                self.numofnum = (-self.end + self.start) // -self.step
            else:
                self.numofnum = (-self.end + self.start - self.step - self.poln) // -self.step

            if -self.numofnum < key < self.numofnum:
                return -(-self.start + key * -self.step)
            else:
                raise IndexError

    def __len__(self) -> int:
        if self.step > 0:
            if self.start > self.end:
                return 0
            self.poln = (self.end - self.start) % self.step
            if self.poln == 0:
                self.numofnum = (self.end - self.start) // self.step
            else:
                self.numofnum = (self.end - self.start + self.step - self.poln) // self.step
        else:
            if self.start < self.end:
                return 0
            self.poln = (-self.end + self.start) % -self.step
            if self.poln == 0:
                self.numofnum = (-self.end + self.start) // -self.step
            else:
                self.numofnum = (-self.end + self.start - self.step - self.poln) // -self.step

        return int(self.numofnum)

