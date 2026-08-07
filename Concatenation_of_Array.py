def getConcatenation(nums):
        nums.extend(nums)
        return nums

nums = [1,2,3]
print(getConcatenation(nums))