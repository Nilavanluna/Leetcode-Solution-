class Solution(object):
    def countPartitions(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ws=0
        fs=0
        c=0
        for i in nums:
            ws+=i
        for i in range(0,len(nums)-1):
            fs+=nums[i]
            ws-=nums[i]
            print(fs,ws)
            if (fs-ws)%2 ==0:
                c+=1

        return c
        
        