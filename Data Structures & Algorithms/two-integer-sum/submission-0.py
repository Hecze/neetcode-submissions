class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nummsLenght = len(nums)
        for i in range(nummsLenght):
            for j in range(i+1, nummsLenght):
                if nums[i] + nums[j] == target:
                    return [i,j]
        return []

        