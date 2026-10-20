class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        counts = {}

        for num in nums: 
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
            
        i = 0
        output=[]
        while i < k:
            most_freq = max(counts, key=counts.get)
            output.append(most_freq)
            del counts[most_freq]
            i +=1

        return output