#User function Template for python3

class Solution:
    def minFind(self, n, a):
        # code here
        red, green, blue = 0, 0, 0
        for i in a:
            if i == "R":
                red += 1
            elif i == "G":
                green += 1
            else:
                blue += 1
        if red == n or green == n or blue == n:
            return n
        if (red % 2 == 0 and green % 2 == 0 and blue % 2 == 0) or (red % 2 == 1 and green % 2 == 1 and blue % 2 == 1):
            return 2
        return 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = input().split()
        
        ob = Solution()
        print(ob.minFind(n, a))
# } Driver Code Ends