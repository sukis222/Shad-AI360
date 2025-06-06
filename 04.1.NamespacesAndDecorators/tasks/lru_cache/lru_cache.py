from collections.abc import Callable
from collections import OrderedDict
from functools import wraps
from typing import Any, TypeVar
from typing_extensions import ParamSpec


P = ParamSpec('P')
T = TypeVar('T')

Function = TypeVar('Function', bound=Callable[..., Any])


def cache(max_size: int) -> Callable[[Callable[P, T]], Callable[P, T]]:
    """
    Returns decorator, which stores result of function
    for `max_size` most recent function arguments.
    :param max_size: max amount of unique arguments to store values for
    :return: decorator, which wraps any function passed
    """
    cache_of_obj: OrderedDict[str, Any] = OrderedDict()
    def decor(func: Callable[P, T]) -> Callable[P, T]:
        @wraps(func)
        def wrapper(*args: P.args, **kwacks: P.kwargs) -> T:
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
        #print(type(wrapper))
        return wrapper

    return decor

