def get_fizz_buzz(n: int) -> list[int | str]:

    sequence = [i for i in range(1, n+1)]
    for i in range(2, n, 3):
        sequence[i] = 'Fizz'
    for i in range(4, n, 5):
        sequence[i] = 'Buzz'
    for i in range(14, n, 15):
        sequence[i] = 'FizzBuzz'
    return sequence

