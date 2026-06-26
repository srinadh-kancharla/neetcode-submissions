class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f={}
        for i in nums:
            if i in f:
                f[i]+=1
            else:
                f[i]=1
        sd=sorted(f.items(),key=lambda x:x[1],reverse=True)
        ans=[]
        for k,v in sd[:k]:
            ans.append(k)
        return ans
        

            
