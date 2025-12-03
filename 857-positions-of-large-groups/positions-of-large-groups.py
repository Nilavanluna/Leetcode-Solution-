class Solution(object):
    def largeGroupPositions(self, s):
        """
        :type s: str
        :rtype: List[List[int]]
        """
        bl=[]
        start=0
        end=0
        for i in range(len(s)-1):
            if s[i]==s[i+1]:
                end=i
            else:
                if i-start>=2:
                    list=[]
                    list.append(start)
                    list.append(end+1)
                    bl.append(list)
                    start=i+1
                    end=i+1
                else:
                    start=i+1
                    end=i+1
        print(start,end)
        if end-start>=1 and s[end]==s[end+1]:
            ll=[]
            ll.append(start)
            ll.append(end+1)
            bl.append(ll)
             
        return bl
        