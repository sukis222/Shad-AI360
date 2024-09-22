def find_value(nums: list[int] | range, value: int) -> bool:
    left = -1
    right = len(nums)

    while right - left > 1:
        mid = (right + left) // 2
        if nums[mid] > value:
            right = mid
        elif nums[mid] < value:
            left = mid
        else:
            return True

    return False
