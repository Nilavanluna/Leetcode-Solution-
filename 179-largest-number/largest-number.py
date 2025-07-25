import functools

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # Convert all numbers to strings
        str_nums = [str(num) for num in nums]

        # Define a custom comparison function
        def compare(n1, n2):
            if n1 + n2 > n2 + n1:
                return -1  # n1 should come before n2
            elif n1 + n2 < n2 + n1:
                return 1   # n2 should come before n1
            else:
                return 0   # They are equal in terms of concatenation

        # Sort the list of strings using the custom comparison function
        # functools.cmp_to_key is used to convert an old-style comparison
        # function to a key function acceptable by sort() or sorted()
        str_nums.sort(key=functools.cmp_to_key(compare))

        # Handle the edge case where all numbers are zero (e.g., [0, 0, 0])
        # In this case, the result should be "0", not "000"
        if str_nums and str_nums[0] == '0':
            return '0'

        # Join the sorted strings to form the largest number
        return "".join(str_nums)