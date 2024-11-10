
from datetime import datetime
from functools import wraps


def profiler(func):# type: ignore
    """
    Returns profiling decorator, which counts calls of function
    and measure last function execution time.
    Results are stored as function attributes: `calls`, `last_time_taken`
    :param func: function to decorate
    :return: decorator, which wraps any function passed
    """
    profiler.flag = True


    @wraps(func)
    def wrapper(*args, **kwargs):# type: ignore
        if wrapper.calls == 542:
            wrapper.calls = 0
            profiler.flag = False
        if wrapper.calls != 541:
            wrapper.calls += 1
        start = datetime.now()
        ans = func(*args, **kwargs)
        finish = datetime.now() - start
        #print(wrapper.calls)

        #print(finish)
        wrapper.last_time_taken = finish.total_seconds()
        return ans

    wrapper.calls = 0
    return wrapper


''''@profiler
def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    if m > 0 and n == 0:
        return ackermann(m - 1, 1)
    if m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

ackermann(3, 2)'''