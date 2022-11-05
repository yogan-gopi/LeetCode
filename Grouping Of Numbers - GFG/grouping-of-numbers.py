#User function Template for python3

class Solution:
    def maxGroupSize(self, arr, N, k):
        # code here 
        ele = [x for x in range(k)]
        mapss = dict.fromkeys(ele, 0)
            
        for i in arr:
            mapss[i%k] += 1
        low, high = 1, (k-1)
        res = 0
        while(low <= high):
            if (low == high) and (mapss[low] > 0):
                res += 1
                break
            
            res = res+max(mapss[low], mapss[high])
            low += 1
            high -= 1
            
        if mapss[0] > 0:
            res += 1
        return res
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.maxGroupSize(arr,N,K))
# } Driver Code Ends