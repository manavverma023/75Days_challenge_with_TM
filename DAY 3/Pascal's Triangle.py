class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ans=[[1]]
        if numRows==1:
            return ans
        elif numRows==2:
            ans.append([1,1])
            return ans
        else:
            ans.append([1,1])
            ind=1
            for i in range(2,numRows):
                s=0
                e=1
                temp=[1]
                for k in range(len(ans[ind])-1):
                    a=ans[ind][s]+ans[ind][e]
                    temp.append(a)
                    s+=1
                    e+=1
                temp.append(1)
                ans.append(temp)
                ind+=1
            return ans

                    
        
        