#User function Template for python3
class Solution:
	def leafNodes(self, arr, N):
		# code here
		stack = []
		res = []
		for i in range(N-1):
		    if arr[i] > arr[i+1]:
		        stack.append(arr[i])
		    elif stack and arr[i+1] > stack[-1]:
		        res.append(arr[i])
		        while stack and stack[-1] < arr[i+1]:
		            stack.pop()
		res.append(arr[N-1])
		return res



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        ob = Solution()
        ans = ob.leafNodes(arr,N)
        for i in range(len(ans)):
            print(ans[i], end = " ")
        print()
# } Driver Code Ends