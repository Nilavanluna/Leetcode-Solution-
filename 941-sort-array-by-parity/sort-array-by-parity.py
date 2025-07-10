class Solution(object):
    def sortArrayByParity(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                continue
            for j in range(i + 1, len(nums)):
            
                if nums[j] % 2 == 0:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
                    break
        return nums
