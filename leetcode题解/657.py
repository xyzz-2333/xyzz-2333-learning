#用时: 4m 22s 
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        list=[0,0]
        for i in range(len(moves)):
            if moves[i]=='R':
                list[0]+=1
            elif moves[i]=='L':
                list[0]-=1
            elif moves[i]=='U':
                list[1]+=1
            elif moves[i]=='D':
                list[1]-=1
        if list==[0,0]:
            return True
        else:return False
#更优的方法
class Solution:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count('U') == moves.count('D') and moves.count('L') == moves.count('R')