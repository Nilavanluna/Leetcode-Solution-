class Solution(object):
    def modifyString(self, s):
        i = 1
        res = ""

        # Convert to list so we can access safely
        n = len(s)

        # Handle first character separately
        if n == 1:
            return "a" if s[0] == "?" else s[0]

        if s[0] != "?":
            res += s[0]
        else:
            # choose a char not equal to s[1]
            for ch in "abcdefghijklmnopqrstuvwxyz":
                if s[1] != ch:
                    res += ch
                    break

        while i < n:
            prev = res[-1]      # already built safe character
            curr = s[i]

            if curr == "?":
                # choose a letter different from previous and next
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    if ch == prev:
                        continue
                    if i < n-1 and s[i+1] != '?' and s[i+1] == ch:
                        continue
                    res += ch
                    break
            else:
                res += curr

            i += 1

        return res
