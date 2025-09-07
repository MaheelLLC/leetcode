class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # neetcode method
        # we have to return a sum that exists so we start with the 
        # first element
        max_sub = nums[0]
        # just intializing the current sum (which also represents 
        # the sub array)
        curr_sum = 0
        # for number in nums
        for num in nums:
            # if the subarray is a negative prefix
            # meaning that the sum of the subarray is negative and 
            # adding this subarray to the next value to test is 
            # pointless
            if curr_sum < 0:
                # restart the subarray (slide its beginning)
                # to where we are right now
                curr_sum = 0
            # now add the next value to the sum
            curr_sum += num
            # if this addition resulted in a higher sum, store it
            max_sub = max(max_sub, curr_sum)

        return max_sub

        # we will have 2 indices to store the ends of the subarray
        l, r = 0, 0
        # a variable to store the maximum sum
        max_sum = max(nums)
        curr_sum = 0
        # while the right end of the subarray hasn't expanded to the end of the array
        while r < len(nums):
            # add the value from the right end of the subarray to current sum
            curr_sum += nums[r]
            # if the current sum is negative, then this entire subarray is useless
            # to continue with
            if curr_sum < 0:
                # move the right end forward into a new subarray
                r += 1
                # move the starting point to the end of the old subarray 
                # (beginning of new subarray)
                l = r
                # set the current sum to zero
                curr_sum = 0
            else:
                # see if we found a new max sum
                max_sum = max(curr_sum, max_sum)
                # now just expand the subarray to the right
                r += 1
        return max_sum















        # Linear solution, time: O(n), space: O(1)
        # Initialize max subarray and current sum
        maxSub = nums[0]
        curSum = 0
        # We iterate through the list
        for n in nums:
            # If the latest number (the number before n) made 
            # the curSum negative, then, from nums[0] or end of 
            # last prefix to said number is 
            # a negative prefix that we can ignore. 
            # Example. [-2, 1, -3...]. -2 is the 
            # first negative prefix, we ignore it. Then, 1, -3 is the
            # second negative prefix, we also ignore that.
            if curSum < 0:
                # Ignore by resetting curSum
                curSum = 0
            # Add the current number 
            curSum += n
            maxSub = max(maxSub, curSum)
        return maxSub

            
            

# Eliminate trailing negative numbers from both ends of list
# This step will be deleted
# while nums and nums[0] < 0:
#     nums.pop(0)
# while nums and nums[-1] < 0:
#     nums.pop(-1)
# Check if list is a single number
# if len(nums) == 1:
#     if nums[0] > 0:
#         return nums[0]
#     else:
#         return 0
# # Check if list is empty
# if not nums:
#     return 0

# valid_starts = {}
# for i, num in enumerate(nums):
#     if num > 0 and (i-1) not in valid_starts:
#         valid_starts[i] = num

# max_sum = 0
# for idx in valid_starts:
#     curr_sum = valid_starts[idx]
#     i = idx + 1
#     while i < len(nums):
#         if nums[i] >= 0:
#             curr_sum += nums[i]
#             i += 1
#         else:
#             health = 0
#             damage = 0
#             j = i
#             while j < len(nums):
#                 if nums[j] < 0:
#                     damage += nums[j]
#                     j += 1
#                 else:
#                     health += nums[j]
#                     j += 1
#             if health > damage:
#                 i = j
#                 curr_sum += (health + damage)
#             else:
#                 break
#     if curr_sum > max_sum:
#         max_sum = curr_sum
# return max_sum
    
"""Observations: 
We want as many positive numbers as possible in the array. However,
if a positive number is followed by a negative number greater in 
absolute value, then the pair subarray is negative in total. It
looks like we can start the subarray with a positive number and then,
keep expanding the subarray with positive numbers. We only want to expand 
with negative numbers if they are less in abs value of the previous positive number. However, in reality it's the sum of the following negative numbers that 
must stay below the latest positive number. So we can iterate through the positive 
numbers as the only valid starting points (maybe make a list of their indices 
in the original list). We can eliminate all starting points that come right after 
(index + 1) another starting point. Then, using my rules for expanding the sub array, we can create the max subarray by finding which starting point expands to 
the highest sum. To simplify the problem, we can eliminate lists that are a 
single number long or lists that are only negative values

Steps
1. Check if len(list) == 1
    if yes, return the single element if positive or return 0 if negative
2. Check if list only has negative values
neg = True
for num in list:
    if num > 0:
        neg = False
        break
if neg:
    return 0
2b. Let's also delete any trailing and starting negative numbers of the list.
i = 0
while list[i] < 0:
    list[i] = 0 or list.pop(i)
    i += 1
i = -1
while list[i] < 0:
    list[i] = 0 or list.pop(i)
    i -= 1
3. Create a new dictionary that holds the indices of valid starting points
valid_starts = {}
for i, num in enumerate(list):
    if num > 0:
        if (i - 1) in valid_starts:
            continue
        else:
            valid_starts[i] = num
4. for each valid start, let's try to create a maximum subarray. We're gonna create
a current sum and largest sum. We set current sum to 0 for every iteration. 
Rules for creating subarray
- If next value is positive, append number to current sum
- If next value is negative, first, create a variable called health_bar. Then, create a damage value. Iterate through list until a positive number is hit. For every iteration, add the current negative value to damage. Once you reach a positive number add it to health_bar, compare health_bar and damage. If health_bar is greater, expand your subarray/current_sum to the positive number.
if current_sum > largest_sum:
    largest_sum = current_sum
return largest_sum
"""