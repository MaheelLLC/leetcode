class Solution:
    def rob(self, nums: List[int]) -> int:
        # to figure out the max of the array[0,i]
        # you must figure out the max between 
        # the max of the subarray[0,i-1] and 
        # the max of the subarray[0,i-2] + array[i]
        # max of subarray[0,i-2]
        max1 = 0
        # max of subarray[0,i-1]
        max2 = 0
        # iterating allows us to expand from the subarrays to the full array
        for num in nums:
            # temp max is the max of current array[0, i]
            temp_max = max(max1 + num, max2)
            # subarray[0,i-1] becomes subarray[0,i-2]
            max1 = max2
            # array[0,i] becomes subarray[0,i-1]
            max2 = temp_max
        return max2
            
class Solution:
    def rob(self, nums: List[int]) -> int:
        prev_1, prev_2 = 0, 0
        rob_max = 0

        for num in nums:
            rob_max = max(prev_1, prev_2 + num)
            prev_2 = prev_1
            prev_1 = rob_max

        return rob_max
            
