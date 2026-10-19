class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        duplicates = set(nums)

        return not (len(duplicates) == len(nums))
