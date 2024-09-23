from typing import List, Union


def get_fizz_buzz(n: int) -> list[int | str]:
    """
        If value divided by 3 - "Fizz",
           value divided by 5 - "Buzz",
           value divided by 15 - "FizzBuzz",
        else - value.
        :param n: size of sequence
        :return: list of values.
        """
    sequence: List[Union[int, str]] = [i for i in range(1, n+1)]

    for i in range(2, n, 3):
        sequence[i] = 'Fizz'
    for i in range(4, n, 5):
        sequence[i] = 'Buzz'
    for i in range(14, n, 15):
        sequence[i] = 'FizzBuzz'
    return sequence
