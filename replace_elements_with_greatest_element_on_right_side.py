class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        # Neetcode solution
        # initial max = -1
        # reverse iteration
        # new max = max(oldmax, arr[i])
        # This method updates the list in reverse order (from last element to first element)
        # Since the last element will no right values, it will become -1
        # Thus, we initialize the right max to the value (-1) that correctly updates the first element
        # in our reverse iteration (remember we're starting with the last element)
        rightMax = -1
        # This for loop iterates from the end of the list until index 0 inclusive. The final value -1 
        # is not included and the step size is now -1
        for i in range(len(arr) - 1, -1, -1):
            # we calculate the new right max for the next iteration using the
            # current max and newly added array value from our iteration
            # You can think of this as expanding the array from the end to the beginning
            # (We're adding a new value for comparision every iteration)
            newMax = max(rightMax, arr[i])
            # We update the array value to the current max
            arr[i] = rightMax
            # And then we truly update the right max for the next iteration
            rightMax = newMax
        return arr

        # My attempt part 2: two pointers
        if len(arr) == 1:
            arr[0] = -1
            return arr
        l, r = 0, 1
        while l < len(arr) - 1:
            right_max = max(arr[l+1:])
            for i in range(l+1,len(arr)):
                if arr[i] == right_max:
                    r = i
                    break
            while l < r:
                arr[l] = arr[r]
                l += 1
        arr[-1] = -1
        return arr

        # My attempt
        for i in range(len(arr) - 1):
            right = arr[i+1]
            for j in range(i+1, len(arr)):
                if arr[j] > right:
                    right = arr[j]
            arr[i] = right
        arr[-1] = -1
        return arr

"""
We want to replace every element except the last one with 
the highest number to the right of it.
Two pointer idea:
let's keep a left pointer on the element that we want to change.
The right pointer will iterate through the rest of the list until it
finds the max number. We can use a max function and then push the right 
pointer until it reaches the max. Once r is at max value, we just 
make every l element equal max until l reaches r. Then we do it again.

Another way is to do it backwards (sounds most optimal). Just compare 
current right max with addition of new right value.
"""