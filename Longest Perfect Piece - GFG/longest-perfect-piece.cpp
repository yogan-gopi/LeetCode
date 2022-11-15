//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

// } Driver Code Ends
class Solution {
  public:
    int longestPerfectPiece(int arr[], int N) {
        // code here
        multiset<int> set;
        int res = 0;
        for(int i=0, j=0; i<N; i++){
            set.insert(arr[i]);
            while(true){
                int maxi = *set.rbegin();
                int mini = *set.begin();
                
                if(maxi - mini > 1){
                    set.erase(set.find(arr[j]));
                    j++;
                }
                else
                    break;
            }
            res =  max(res, (int)set.size()); 
        }
        return res;
    }
};

//{ Driver Code Starts.
int main() {
    int t;
    cin >> t;
    while (t--) {
        int N;
        
        cin>>N;
        int arr[N];
        for(int i=0; i<N; i++)
            cin>>arr[i];

        Solution ob;
        cout << ob.longestPerfectPiece(arr,N) << endl;
    }
    return 0;
}
// } Driver Code Ends