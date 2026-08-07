#Question: Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).Return the running sum of nums.

#Input: nums = [1,2,3,4]
#Output: [1,3,6,10]
#Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

def runningSum(nums):
    output_list = []
    output_list.append(nums[0])
    for i in range (1,len(nums)):
        output_list.append(nums[i]+output_list[(len(output_list)-1)])
    return(output_list)

nums = [1,1,1,1,1]
print(runningSum(nums))