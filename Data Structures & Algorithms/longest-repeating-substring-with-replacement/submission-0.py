class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        
        l = 0
        maxf = 0
        for r in range(len(s)):
            # Update frequency of the current character
            count[s[r]] = 1 + count.get(s[r], 0)
            # Update the max frequency found in the current window
            maxf = max(maxf, count[s[r]])
            
            # If (window length - most frequent char count) > k, it's invalid
            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
            
        return res

        