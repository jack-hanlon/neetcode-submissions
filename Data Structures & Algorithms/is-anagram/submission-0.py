class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = {}
        count_t = {}

        for i in range (0,len(s)):
            if s[i] not in count_s:
                count_s[s[i]] = 1
            else:
                count_s[s[i]] +=1

        for j in range (0,len(t)):
            if t[j] not in count_t:
                count_t[t[j]] = 1
            else:
                count_t[t[j]] +=1

        if count_s == count_t:
            return True

        return False