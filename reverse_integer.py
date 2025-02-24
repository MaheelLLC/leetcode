class Solution:
    def reverse(self, x: int) -> int:
        # Neetcode solution
        # Integer.MAX_VALUE = 2147483647 (end with 7)
        # Integer.MIN_VALUE = -2147483648 (end with -8)
        MIN = -2147483648 # -2^31
        MAX = 2147483647 # 2^31 - 1
        # Result is initially 0
        # Result represents the reversed number that we want to output
        res = 0
        # while integer x is not zero, we will go through each digit of x
        while x:
            # x mod 10 will equal the current digit we want
            # Python sucks at math so we have to use math.fmod
            digit = int(math.fmod(x, 10)) # (python dumb) -1 % 10 = 9
            # Then we iterate to the next digit by chopping off the current digit
            # We can't use x // 10 since python sucks at math
            x = int(x / 10) # (python dumb) -1 // 10 = -1

            # Before I add the digit to the result, let's just make sure the
            # result is still within the constraints. All these next two
            # if statements do is check if result is overflowing past the constraints
            # of the 32 bit integer.
            
            # If result is greater than MAX (from its tens to final place since
            # we are adding another digit to result: 214748364) or
            # if result equals MAX's rest of digits besides one's place, but 
            # result's ones place (the current digit that we are adding) is
            # greater than MAX's ones place (7). Then we return zero.
            if (res > MAX // 10 or 
                (res == MAX // 10 and digit > MAX % 10)):
                return 0

            # Now, if result is less than MINs rest of digits (-214748364)
            # or result equals MINs rest of digits (-214748364, missing ones place)
            # and current digit is more negative than MIN's ones place (-8), we return
            # zero
            if (res < MIN // 10 or 
                (res == MIN // 10 and digit < MIN % 10)):
                return 0
            
            # Now, let's shift the digits already in result by multiplying result by
            # 10 and then adding our current digit
            res = (res * 10) + digit
        return res
        # My attempt
        if x < 0:
            x *= -1
            flipped = [i for i in str(x)]
            flipped.reverse()
            flipped = ["-"] + flipped
        else:
            flipped = [i for i in str(x)]
            flipped.reverse()

        num = int("".join(flipped))
        if num > (2**31 - 1) or num < -2**31:
            return 0
        else:
            return num
        
