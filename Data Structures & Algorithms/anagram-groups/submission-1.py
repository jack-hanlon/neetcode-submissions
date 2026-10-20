class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    
        groups = {}

        for i in range(0, len(strs)):
            srtd = "".join(sorted(strs[i]))
            if srtd not in groups:
                groups[srtd] = [strs[i]]
            elif srtd in groups: 
                groups[srtd].append(strs[i])

        return list(groups.values())