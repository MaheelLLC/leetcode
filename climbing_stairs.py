class Solution:
    def climbStairs(self, n: int) -> int:
        # we need two variables to store the number of combinations of 1 and 2 steps before
        step_1 = 1
        step_2 = 1
        # we need a variable to store the current number of combinations
        curr_step = 0
        # let's cover the base cases
        if n == 1:
            return 1
        elif n == 2:
            return 2
        for i in range(n - 1):
            # the number of combinations in the current step is just 
            # the sum of the previous two combinations
            curr_step = step_1 + step_2
            # now 1 step before is 2 steps before
            step_2 = step_1
            # the current step is now 1 step before
            step_1 = curr_step
        return curr_step
            