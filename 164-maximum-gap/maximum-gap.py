class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max=0
        nums= sorted(nums)
        if len(nums)<2:
            return 0
        for i  in range(1,len(nums)):
            if nums[i]-nums[i-1]>max:
                max=nums[i]-nums[i-1]
                print(max)
        return max
