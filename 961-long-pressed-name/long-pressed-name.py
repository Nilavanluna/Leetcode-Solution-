class Solution(object):
    def isLongPressedName(self, name, typed):
        a1 = 0
        a2 = 0
        prev = name[0]

        while a1 < len(name) and a2 < len(typed):
            print(name[a1], typed[a2], prev)

            if name[a1] == typed[a2]:
                prev = name[a1]     # update prev correctly
                a1 += 1
                a2 += 1
            else:
                if typed[a2] == prev:
                    a2 += 1
                else:
                    return False

        # If name still has characters left, typed is too short
        if a1 < len(name):
            return False

        # Remaining typed chars must match last valid prev
        while a2 < len(typed):
            if typed[a2] != prev:
                return False
            a2 += 1

        return True
