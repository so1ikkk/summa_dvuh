def twosum(nums, target):
    for m in range(len(nums)):
        for n in range(m + 1, len(nums)):
            if nums[m] + nums[n] == target:
                return [m, n]