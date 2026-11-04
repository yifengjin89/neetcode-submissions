class Solution:
    def isPalindrome(self, s: str) -> bool:
        # To solve if string match its reverse order, I use two pointers.
        # Set 1 pointer at the start and another pointer at the end of the string
        # then move two pointers to the oppisite way, if they are diff character, which
        # means not Palindrome, otherwise continue move until they meet each other.
        # Time complexicy is O(n), where n is the size of string becuase each character would
        # be visited at most onec, we don't use extra space so is O(1)

        start = 0
        end = len(s) - 1
        while start < end:
            while start < end and not s[start].isalnum():
                start += 1
            while start < end and not s[end].isalnum():
                end -= 1

            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        
        return True
            