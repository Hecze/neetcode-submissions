class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        readed = set([])
        for num in nums:
            if num in readed:
                return True
            readed.add(num)
        return False
        