class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        left_products = []

        for i in range(0,len(nums)):
            if i == 0:
                left_products.append(1)
            else:
                left_products.append(nums[i-1]*left_products[i-1])
        

        right_products=[]

    

        for j in range(len(nums) - 1, -1, -1):
            if j == len(nums)-1:
                right_products.append(1)
            else:
                right_products.append(nums[j+1]*right_products[-1])

        right_products = right_products[::-1]

        products = []
        for i in range(0,len(nums)):
            products.append(left_products[i]*right_products[i])

        return products
