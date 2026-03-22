'''class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(martix):
            martix2=martix
            for i in range(len(martix2)):          #行
                for j in range(len(martix2[i])):   #列
                    martix2[i][j],martix2[j][i]=martix[j][i],martix[i][j]#转置
            for i in range(i+1,len(martix)):
                martix[i].reverse()
            return martix2
        for i in range(4):
            if target== mat:
                return True
            mat=rotate(mat)
        return False'''
class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(martix):
            for i in range(len(martix)):          #行
                for j in range(i+1,len(martix[i])):   #列
                    martix[i][j],martix[j][i]=martix[j][i],martix[i][j]#转置
            for i in range(len(martix)):
                martix[i].reverse()
            return martix
        for i in range(4):
            if target== mat:
                return True
            mat=rotate(mat)
        return False
if __name__=='__main__':
    example=[[1,2,3],
            [4,5,6],
            [7,8,9]] 
    
    example[1][2] = 'a'
    print(example) 
    