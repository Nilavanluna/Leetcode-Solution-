class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        count1=Counter(ransomNote)
        count2=Counter(magazine)

        for char in count1:
            if count1[char]>count2.get(char,0)  :
                return False

        return True
        