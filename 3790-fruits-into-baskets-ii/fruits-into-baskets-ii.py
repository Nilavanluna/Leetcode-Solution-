class Solution(object):
    def numOfUnplacedFruits(self, fruits, baskets):
        
      for i in range(len(baskets)):
         for j in range(len(baskets)):
            if fruits[i]<=baskets[j]:
               baskets.pop(j)
               break
      return len(baskets)