class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        l1=self.binary(x)
        l2=self.binary(y)
        res=k=0
        max_len = max(len(l1), len(l2))
        l1 += [0] * (max_len - len(l1))
        l2 += [0] * (max_len - len(l2))
        while k<len(l1) and k<len(l2):
            if l2[k]!=l1[k]:
                res+=1
            k+=1
        return res
    def binary(sef, num):
        list=[]

        while num>0:
            list.append(num%2)
            num=num//2
        
        return list