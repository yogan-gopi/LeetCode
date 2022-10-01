class Solution {
public:
    int add(int n){
            int sum = 0;
            while (n > 0){
                sum+=(n%10);
                n /= 10;
            }
            return sum;
        }
    int addDigits(int num) {
        
        if(num == 0){
            return num;
        }
        while(num>9){
            num = add(num);
        }
        return num;
    }
};