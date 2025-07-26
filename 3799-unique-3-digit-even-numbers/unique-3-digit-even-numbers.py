class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        seti=set()
        n=len(digits)
        for i in range(n):
                    for j in range(n):
                                for k in range(n):
                                    if i!=j and j!=k and i!=j and i!=k and digits[i]!=0:
                                     digit=digits[i]*100+digits[j]*10+digits[k]
                                     if digit%2==0:
                                        seti.add(digit)
        print(seti)
        return len(seti)


        