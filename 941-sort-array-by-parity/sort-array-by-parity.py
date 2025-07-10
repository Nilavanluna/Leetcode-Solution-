class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        p1=0
        p2=len(nums)-1
        print(p2)
        while p1<p2:
            if nums[p1]%2==1:
                if nums[p2]%2==0:
                 temp=nums[p1]
                 nums[p1]=nums[p2]
                 nums[p2]=temp
                 p2-=1
                 p1+=1
                else:
                    p2-=1
                
            else:
                p1+=1


        return nums
