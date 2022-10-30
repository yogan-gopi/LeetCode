#User function Template for python3

class Solution:
	def NoOfChicks(self, N):
		# Code here
		arr = [0 for _ in range(50)]
		res = 1
		arr[6] = 1
		for i in range(1, N):
		    res -= arr[i]
		    arr[i+6] += 2*res
            res += 2*res
        return res
        
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		N = int(input())
		obj = Solution()
		ans = obj.NoOfChicks(N)
		print(ans)

# } Driver Code Ends