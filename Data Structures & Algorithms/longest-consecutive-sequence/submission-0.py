class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        numSet = set(nums)  
        longest = 0       

        for num in numSet:
            if (num - 1) not in numSet:
                # This is the start of a sequence
                step = 1
                while (num + step) in numSet:
                    step += 1
                longest = max(step, longest)

        return longest            
        