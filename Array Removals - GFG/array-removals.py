#User function Template for python3


class Solution:

	def removals(self,arr, n, k):
	    dp = {}
	    def rec(i, j, arr, k):
	        if i > j: return 0
	        
	        if arr[j]-arr[i] <= k: return 0
	        if (i, j) in dp:
	            return dp[(i, j)]
	        
	        op1 = rec(i+1, j, arr, k)
	        op2 = rec(i, j-1, arr, k)
	        
	        dp[(i, j)] = min(op1,op2)+1
	        return dp[(i, j)]
	        
		# code here
		arr.sort()
		return rec(0, n-1, arr, k)
		    
		


#{ 
 # Driver Code Starts
#Initial Template for Python 3


if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.removals(arr, n, k)
        print(ans)
        tc -= 1
# } Driver Code Ends