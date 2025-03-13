class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Neetcode solution T: O(log(n))
        # left and right pointers
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid
            
            # Checks whether target is greater than mid
            if target > nums[mid]:
                l = mid + 1
            # Checks whether target is less than mid
            else:
                r = mid - 1
        
        # Why are we returning the left pointer?
        # This is the case when the target value is never
        # found in the list
        return l

        # My attempt
        first = 0
        last = len(nums) - 1
        found = False
        while not found: 
            mid = (first + last) // 2
            if first >= last:
                break
            elif nums[mid] > target:
                last = mid - 1
                if last < 0:
                    last = 0
            elif nums[mid] < target:
                first = mid + 1
                if first == len(nums):
                    first = len(nums) - 1
            elif nums[mid] == target:
                found = True

        if found:
            return mid
        else:
            if nums[last] < target:
                return last + 1
            else:
                return last