class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s = {}
        count_t = {}
        for i in range(len(s)):
            l1 = s[i]
            l2 = t[i]
            if l1 in count_s:
                count_s[l1] += 1
            else:
                count_s[l1] = 1
            if l2 in count_t:
                count_t[l2] += 1
            else:
                count_t[l2] = 1
        return count_s == count_t