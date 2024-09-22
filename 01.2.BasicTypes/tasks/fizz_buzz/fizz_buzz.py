def get_fizz_buzz(n: int) -> list[int | str]:
    nums = [i for i in range(1, n+1)]
    for i in range(2, n, 3):
        nums[i] = "Fizz"
    for i in range(4, n, 5):
        nums[i] = "Buzz"
    for i in range(14, n, 15):
        nums[i] = "FizzBuzz"
    return nums
