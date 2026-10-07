class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        postfix = [0] * len(nums)
        prod = 1;
        for i in range(len(nums)):
            if i == 0:
                prefix[i] = 1
                continue
            prod *= nums[i-1]
            prefix[i] = prod
        prod = 1;
        for j in range(len(nums)-1, -1,-1):
            if(j == len(nums)-1):
                postfix[j] = 1
                continue
            prod *= nums[j+1]
            postfix[j] = prod
        result = [0] * len(nums)
        for x in range(len(nums)):
            result[x] = prefix[x] * postfix[x]
        return result