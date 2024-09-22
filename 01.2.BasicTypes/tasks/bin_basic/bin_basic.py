def find_value(nums: list[int] | range, value: int) -> bool:
    left = 0
    right = len(nums)
    if right > 0:
        if nums[left] == value:
            return True
    while right - left > 1:
        mid = (right + left) // 2
        if nums[mid] > value:
            right = mid
        elif nums[mid] <= value:
            left = mid
        if nums[left] == value:
            return True
        print(mid)
    return False

d = list(map(int, input().split()))
a = int(input())
print(find_value(d, a))