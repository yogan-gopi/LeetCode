#User function Template for python3
class Solution:
    def twoOddNum(self, Arr, N):
        # code here
        res = []
        freq = {}
        for i in Arr:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        for i in freq:
            
            if freq[i]%2 == 1:
                res.append(i)
            if len(res) == 2:
                return sorted(res, reverse = True)
        



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        Arr = input().split()
        for itr in range(N):
            Arr[itr] = int(Arr[itr])
        ob = Solution();
        ans = ob.twoOddNum(Arr,N)
        for i in range(len(ans)):
        	print(ans[i], end = " ")
        print()
# } Driver Code Ends