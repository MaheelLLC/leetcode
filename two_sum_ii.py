class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1
        curr_sum = numbers[left] + numbers[right]
        while curr_sum != target:
            if curr_sum < target:
                left += 1
            else:
                right -= 1
            curr_sum = numbers[left] + numbers[right]
        return [left + 1, right + 1]
    
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            total = numbers[left] + numbers[right]

            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                return [left + 1, right + 1]