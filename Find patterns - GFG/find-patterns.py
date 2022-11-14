#User function Template for python3
class Solution:
    def numberOfSubsequences (self,S,W):
        # code here 
        n1 = len(S)
        n2 = len(W)
        ans = 0
        vis = [False for _ in range(n1)]
        for i in range(n1):
            if S[i] == W[0] and not vis[i]:
                vis[i] = True
                j = i+1
                k = 1
                while j < n1 and k < n2:
                    if S[j] == W[k] and not vis[j]:
                        vis[j] = True
                        k += 1
                    j += 1
                if k ==  n2:
                    ans += 1
                else:
                    break
        return ans


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())
        W=str(input())

        ob = Solution()
        print(ob.numberOfSubsequences(S,W))

# } Driver Code Ends