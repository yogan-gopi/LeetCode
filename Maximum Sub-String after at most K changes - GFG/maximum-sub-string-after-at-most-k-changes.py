#User function Template for python3

class Solution:
	def characterReplacement(self, s, k):
		# Code here
		count = {}
		res = 0
		l = 0
		mf = 0
		for r in range(len(s)):
		    count[s[r]] = 1+count.get(s[r], 0)
		    mf = max(mf, count[s[r]])
		    while (r-l+1) - mf > k:
		        count[s[l]] -= 1
		        l += 1
		    
		    res = max(res, r-l+1)
	    return res
        

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		k = int(input())
		ob = Solution()
		ans = ob.characterReplacement(s, k)
		print(ans)

# } Driver Code Ends