#User function Template for python3

class Solution:
	def totalWays(self, n, capacity):
		# code here
		capacity.sort()
		res = capacity[0]
		for i in range(1, n):
		    res = (res*(capacity[i]-i))%(10**9+7)
		return res % (10**9+7)


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n= int(input())
		capacity = list(map(int,input().split()))
		ob = Solution()
		ans = ob.totalWays(n,capacity)
		print(ans)

# } Driver Code Ends