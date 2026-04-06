#第一版，会超时
def robotSim(commands, obstacles) -> int:
    #directions = [W,D,S,A]
    index,dis = 0,0
    coord=[0,0]
    def right(index):
        return (index + 1) % 4
    def left(index):
        return (index -1) % 4
    def can_move(index,coord):
    #判断前面是不是墙，没墙则返回True
        if obstacles==[]:
            return True
        pos=list(coord)
        if index== 0:
            pos[1]+=1
        elif index== 1:
            pos[0]+=1
        elif index== 2:
            pos[1]-=1
        elif index== 3:
            pos[0]-=1
        if pos in obstacles:#过不了再优化
            return False
        else: return True
    def move(index):
        if index== 0:
            coord[1]+=1
        elif index== 1:
            coord[0]+=1
        elif index== 2:
            coord[1]-=1
        elif index== 3:
            coord[0]-=1
    for i in range(len(commands)):
        if commands[i]==-1:
            index = right(index)
        elif commands[i]==-2:
            index = left(index)
        else:
            for j in range(commands[i]):
                if can_move(index,coord):
                    move(index)
                    if coord[0]**2+coord[1]**2 > dis:
                        dis = coord[0]**2+coord[1]**2
                else: break
                #print(f'位置：{coord} 方向：{index} 最大距离：{dis}')
    return dis
def robotSim(commands, obstacles) -> int:
    #directions = [W,D,S,A]
    index,dis = 0,0
    coord=[0,0]
    obstacle_set = set(tuple(obs) for obs in obstacles)
    def right(index):
        return (index + 1) % 4
    def left(index):
        return (index -1) % 4
    def can_move(index,coord):
    #判断前面是不是墙，没墙则返回True
        '''        if obstacles==[]:
            return True
        会超时的大输入不会是空的'''
        pos=list(coord)
        if index== 0:
            pos[1]+=1
        elif index== 1:
            pos[0]+=1
        elif index== 2:
            pos[1]-=1
        elif index== 3:
            pos[0]-=1
        if tuple(pos) in obstacle_set:
            return False
        else: return True
    def move(index):
        if index== 0:
            coord[1]+=1
        elif index== 1:
            coord[0]+=1
        elif index== 2:
            coord[1]-=1
        elif index== 3:
            coord[0]-=1
    for i in range(len(commands)):
        if commands[i]==-1:
            index = right(index)
        elif commands[i]==-2:
            index = left(index)
        else:
            for j in range(commands[i]):
                if can_move(index,coord):
                    move(index)
                    if coord[0]**2+coord[1]**2 > dis:
                        dis = coord[0]**2+coord[1]**2
                else: break
                #print(f'位置：{coord} 方向：{index} 最大距离：{dis}')
    return dis
if __name__=='__main__':
    robotSim([4,-1,4,-2,4],[[2,4]])