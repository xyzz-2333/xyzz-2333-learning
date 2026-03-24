class Solution:
    def constructProductMatrix(self, grid) : #List[List[int]]-> List[List[int]]:
        matrix = [[0] *len(grid[0])  for _ in range(len(grid))]
        for i in range(len(grid)):          #行
            for j in range(len(grid[0])):   #列
                #遍历矩阵每个元素
                r=1
                for k in range(len(grid)):          #行
                    for l in range(len(grid[0])):   #列
                        if k==i and l==j:
                             pass
                        else: r=r*grid[k][l]
                r=r%12345
                matrix[i][j]=r         
        return matrix



if __name__=='__main__':
    example=[
            [1,2,3],
            [4,5,6],
            [7,8,9]] 
    grid = [[1,2],
            [3,4],
            [5,6]]
    matrix = [[0] *len(grid[0])  for _ in range(len(grid))]
    print(matrix)