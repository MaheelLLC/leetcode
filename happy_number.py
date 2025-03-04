class Solution:
    def isHappy(self, n: int) -> bool:
        # Tortoise and Hare principle
        # This function gives sum of squared digits
        # It represents the next number we go to when we perform this calculation
        def get_next(num):
            # Intialize the next number
            total = 0
            # While the previous number is not 0
            while num:
                # Collect its right most digit
                digit = num % 10
                # Square said digit
                digit = digit ** 2
                # Delete the digit off of num/previous number
                num //= 10
                # Add squared digit to next number
                total += digit
            return total
        # Start tortoise at first number
        turtle = n
        # Start hare at second number
        hare = get_next(n)
        # If it's a happy number, hare will get to 1 first
        # If it's not a happy number, turtle and hare will meet up
        while hare != 1 and turtle != hare:
            # Make hare go two numbers ahead of itself
            hare = get_next(get_next(hare))
            # Make tortoise go one number ahead of itself
            turtle = get_next(turtle)
        return hare == 1
        
        # Neetcode: same strategy but used/visit is more efficient
        # Can be done better with a linked list
        visit = set() # Memory O(n)
        while n not in visit:
            visit.add(n)
            n = self.sum_of_squares(n)

            if n == 1:
                return True
    
        return False

    def sum_of_squares(self, n: int) -> int:
        output = 0
        while n:
            digit = n % 10
            digit = digit**2
            output += digit
            n = n // 10
        return output
        

"""
# My attempt
        total = 0
        n = [int(x)**2 for x in str(n)]
        used = []
        while total != 1:
            total = sum(n)
            if total in used:
                return False
            else:
                used.append(total)
            n = [int(x)**2 for x in str(total)]
        return True
"""