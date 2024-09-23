def find_value(nums: list[int] | range, value: int) -> bool:
    """
        Find value in sorted sequence
        :param nums: sequence of integers. Could be empty
        :param value: integer to find
        :return: True if value exists, False otherwise
        """
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
    return False
