#User function Template for python3

class alphanumeric:
    def __init__(self,name,count):
        self.name=name
        self.count=count
class Solution:
    def sortedStrings(self,N,A):
        #code here
        res = []
        freq = {}
        for i in A:
            if i not in freq:
                freq[i] = 0
            freq[i] += 1
        for i in sorted(freq):
            obj = alphanumeric(i, freq[i])
            res.append(obj)
        return res
            
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        N=int(input())
        a=[]
        for i in range(N):
            x=input()
            a.append(x)
        ob=Solution()
        ans=ob.sortedStrings(N,a)
        for i in ans:
            print(i.name,end=" ")
            print(i.count)
# } Driver Code Ends