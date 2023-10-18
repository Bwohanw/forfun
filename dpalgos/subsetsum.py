'''
The problem: Given a list of numbers and a target T, find if a subset of
 numbers from the list sum to the target'''


nums = [8,6,7,5,3,10,9]
target = 15


def subsetSum(idx, remainder):
    if (remainder == 0):
        return True
    if (remainder < 0 or idx >= len(nums)):
        return False
    return (subsetSum(idx+1,remainder-nums[idx])) or subsetSum(idx+1,remainder)

print(subsetSum(0,target))