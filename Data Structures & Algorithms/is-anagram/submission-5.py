class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {} , {}
        for i in range(len(s)):
            l1, l2 = s[i], t[i]
            count_s[l1] = count_s.get(l1, 0) + 1
            count_t[l2] = count_t.get(l2, 0) + 1
        return count_s == count_t