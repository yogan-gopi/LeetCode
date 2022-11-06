#User function Template for python3

class Solution:
    def minPartition(self, N):
        # code here 
        den = (2000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
        res = []
        i = 0
        while(i < len(den)):
            if N//den[i] > 0:
                tem = N//den[i]
                for _ in range(tem):
                    res.append(den[i])
                N = N-(den[i]*tem)
            i+=1
        return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        arr = ob.minPartition(N)
        for i in range(len(arr)):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends