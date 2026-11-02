class Solution:
    def isPalindrome(self, s: str) -> bool:

        s_no_spaces = re.sub(r'[\W_]', '', s).lower()

        left, right = 0, len(s_no_spaces)-1

        while left < right:
            if s_no_spaces[left] != s_no_spaces[right]:
                return False
            left = left + 1
            right = right - 1

        return True