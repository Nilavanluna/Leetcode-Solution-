class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res=[]
        def back(i,parts):
            if len(parts)==4:
                if i==len(s):
                    res.append(".".join(parts))
                return
            for l in range(1,4):
                if i+l > len(s):
                    break
                segment=s[i:i+l]
                if segment[0]=="0" and len(segment)>1:
                    continue
                if int(segment)>255:
                    continue
                back(i+l,parts+[segment])
        back(0,[])
        return res
                    
        