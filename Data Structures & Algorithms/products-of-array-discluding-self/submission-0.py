class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [1] * n

        # Step 1 : Calculate Prefix Products
        # Store  in res[i] the product of  all elements to 
        prefix =  1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        # Step 2: Calcute Suffix Products on the fly
        # Multiply res[i] by the product of all elements to the right of i
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
        return res