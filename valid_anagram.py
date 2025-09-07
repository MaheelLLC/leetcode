class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for letter in s:
            if letter in s_dict:
                s_dict[letter] += 1
            else:
                s_dict[letter] = 1
        
        for letter in t:
            if letter in t_dict:
                t_dict[letter] += 1
            else:
                t_dict[letter] = 1
        
        return s_dict == t_dict



        # # My methods
        # # Time complexity: O(n)
        # # Space complexity: O(1)
        # # Actually this method may fail
        # if len(s) != len(t):
        #     return False
        # for letter in t:
        #     try:
        #         s.replace(letter, "", 1)
        #     except:
        #         return False
        # if s == "":
        #     return True
        # # Time complexity: O(n^2)
        # # Space complexity: O(n)
        # ana_dict = {}
        # for letter in s:
        #     if letter in ana_dict.keys():
        #         ana_dict[letter] += 1
        #     else:
        #         ana_dict[letter] = 1
        # for letter in t:
        #     if letter not in ana_dict.keys() or ana_dict[letter] == 0:
        #         return False
        #     else:
        #         ana_dict[letter] -= 1
        # return True

        # Neetcode hashmap solution
        if len(s) != len(t):
            return False
        countS, countT = {}, {}
        for i in range(len(s)):
            countS[s[i]] = 1 + countS.get(s[i], 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False
        return True

        # Cheat method
        return Counter(s) == Counter(t)

        # Neetcode sorted solution
        return sorted(s) == sorted(t)





"""Another method is to replace each s character with an empty string for every matching character in t.
for letter in t:
    try:
        s.replace(letter, "", 1)
    except:
        return False
if s == "":
    return True
"""