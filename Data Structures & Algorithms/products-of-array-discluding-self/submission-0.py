class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pro=1
        zero=0
        for i in nums:
            if i!=0:
                pro*=i
            else:
                zero+=1
        if zero==0:
            ans=[pro//i for i in nums]
        elif zero>1:
            ans=[0 for i in nums]
        else:
            ans=[0 if i!=0 else pro for i in nums]
        return ans