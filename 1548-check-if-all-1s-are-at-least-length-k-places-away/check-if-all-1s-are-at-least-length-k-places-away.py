class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        i=0
        cz=0
        of=False
        while i < len(nums):
          if nums[i]==0:
            cz+=1
          else:
            if cz<k and i!=0 and of==True:
                return False
            cz=0
            of=True
          i+=1
       



        return True        
        