def missingNumber(nums: list[int]) -> int:
    sum_nums = sum(nums)
    return (len(nums) + 1) * len(nums) // 2 - sum_nums

print(missingNumber([0, 1, 2, 4, 3]))
