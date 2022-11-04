#User function Template for python3
import math
class Solution:
	def baseEquiv(self, n, m):
		# code here
		for i in range(2, 33):
		    num = math.log(n, 10)//math.log(i, 10) + 1
		    
		    if num == m:
		        return "Yes"
	    return "No"



#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		n,m = input().split()
		n=int(n)
		m=int(m)
		ob = Solution();
		print(ob.baseEquiv(n,m))

# } Driver Code Ends