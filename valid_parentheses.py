        stack = []
        closeToOpen = {")" : "(", "]" : "[", "}" : "{"}

        for i in range(len(s)):
            #check if its an opening (anything not in the map)
            if s[i] not in closeToOpen:
                stack.append(s[i])
            elif stack and closeToOpen[s[i]] == stack[-1]:
                stack.pop()
            else:
                return False
            
        return not stack

























        # # Neetcode solution
        # stack = []
        # close_to_open = { ")" : "(", "}" : "{", "]" : "[" }
        
        # for c in s:
        #     if c in close_to_open:
        #         if stack and stack[-1] == close_to_open[c]:
        #             stack.pop()
        #         else:
        #             return False
        #     else:
        #         stack.append(c)
        
        # return True if not stack else False

        # # My attempt T O(n) S or M O(n)
        # stack = []
        # hash_map = {')':'(', '}':'{', ']':'['}
        # for char in s:
        #     if char in "({[":
        #         stack.append(char)
        #     elif char in ")}]":
        #         if not stack or hash_map[char] != stack[-1]:
        #             return False
        #         else:
        #             stack.pop()
        # if stack:
        #     return False
        # return True