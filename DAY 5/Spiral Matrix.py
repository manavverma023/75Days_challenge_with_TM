class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans=[]
        while matrix:
            ans+=matrix.pop(0)
            matrix=[*zip(*matrix)][::-1]
            print(matrix)
        else:
            return ans