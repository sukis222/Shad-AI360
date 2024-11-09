from collections.abc import Callable
from collections import OrderedDict
from functools import wraps
from typing import Any, TypeVar


Function = TypeVar('Function', bound=Callable[..., Any])


def cache(max_size: int) -> Callable[[Function], Function]:
    """
    Returns decorator, which stores result of function
    for `max_size` most recent function arguments.
    :param max_size: max amount of unique arguments to store values for
    :return: decorator, which wraps any function passed
    """
    cache_of_obj: OrderedDict[str, Any] = OrderedDict()
    def decor(func) -> Function:
        @wraps(func)
        def wrapper(*args, **kwacks) -> Function:
            if cache_of_obj.get(str(args) + str(kwacks)) is None:
                while len(cache_of_obj) >= max_size:
                    for elem in cache_of_obj:
                        cache_of_obj.pop(elem)
                        break
                cache_of_obj[str(args) +  str(kwacks)] = func(*args, **kwacks)
                cache_of_obj.move_to_end(str(args) +  str(kwacks))
                return cache_of_obj[str(args) + str(kwacks)]
            else:
                return cache_of_obj[str(args) +  str(kwacks)]
        return wrapper

    return decor



'''@cache(7)
def binomial(n: int, k: int) -> int:
    if k > n:
        return 0
    if k == 0:
        return 1
    return binomial(n - 1, k) + binomial(n - 1, k - 1)

binomial(8, 4)
print(help(binomial))'''

