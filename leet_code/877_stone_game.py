# https://leetcode.com/problems/stone-game/


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        l, r= 0, len(piles)-1
        alex, lee=0, 0
        turn = 0
        while(l<=r):
            if turn==0:
                if piles[l]<piles[r]:
                    alex+=piles[r]
                    r-=1
                else:
                    alex+=piles[l]
                    l+=1

            elif turn==1:
                if piles[l]<piles[r]:
                    lee+=piles[l]
                    l+=1
                else:
                    lee+=piles[r]
                    r-=1
            turn=(turn+1)%2

        return True if alex>lee else False