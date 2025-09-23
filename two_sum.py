class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differences = {}

        for index, num in enumerate(nums):
            if num in differences:
                return [differences[num], index]
            
            differences[target - num] = index
        
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # we need a difference dictionary
        difference = {}
        for i in range(len(nums)):
            if nums[i] in difference:
                return [difference[nums[i]], i]
            difference[target - nums[i]] = i
        
        return False


        # My method
        # Time: O(n^2)
        # Space O(1)
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]

        # My attempt with neetcode's idea
        # Time: O(n)
        # Space: O(n)
        # hash_map = {}
        # for i in range(len(nums)):
        #     diff = target - nums[i]
        #     if diff in hash_map.keys():
        #         return [i, hash_map[diff]]
        #     else:
        #         hash_map[nums[i]] = i

        # Neetcode solution
        prevMap = {} # val : index (val means the number element in nums)
        # The values of the hashmap are indices
        for i, n in enumerate(nums):
            # Looking at our current integer element
            # First, we find out our desired second number that sums up
            # with the current element to equal the target
            # We do this by subtracting the target by the current element
            # Our desired number is the difference.
            diff = target - n
            # If our desired number is in our hashmap meaning that
            # it exists in our list
            if diff in prevMap:
                # We can return its index (hashmap value) and the index
                # of the current element
                return [prevMap[diff], i]
            prevMap[n] = i