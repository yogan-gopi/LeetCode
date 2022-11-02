from typing import List


from typing import List


class Solution:
    def largestArea(self,n:int,m:int,k:int, enemy : List[List[int]]) -> int:
        # code here
        rows = [0]
        col = [0]
        res = n*m
        for i in enemy:
            rows.append(i[0])
            col.append(i[1])
        rows.append(n+1)
        col.append(m+1)
        rows.sort()
        col.sort()
        maxR = 0
        maxC = 0
        for i in range(1, len(rows)):
            maxR = max(maxR, rows[i]-rows[i-1]-1)
        for i in range(1, len(col)):
            maxC = max(maxC, col[i]-col[i-1]-1)
        
        return maxR*maxC



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(3)
        n,m,k=a[0],a[1],a[2]
        
        e=IntMatrix().Input(a[2], 2)
        
        obj = Solution()
        res = obj.largestArea(n,m,k, e)
        
        print(res)
        

# } Driver Code Ends