class Solution {
    public int calculate(String s) {
        int len = s.length();
        int sign = 1;
        int res = 0;
        int cur = 0;
        Stack<Integer> stack = new Stack<Integer>();
        
        for(int i = 0; i<len; i++){
            if(Character.isDigit(s.charAt(i))){
                cur = s.charAt(i) - '0';
                while(i+1 < len && Character.isDigit(s.charAt(i+1))){
                    cur = cur*10 + s.charAt(i+1) - '0';
                    i++;
                }
                cur = cur*sign;
                res += cur;
                cur = 0;
                sign = 1;
            }
            else if(s.charAt(i) == '+')
                sign = 1;
            else if(s.charAt(i) == '-')
                sign = -1;
            else if(s.charAt(i) == '('){
                stack.push(res);
                stack.push(sign);
                res = 0;
                sign = 1;
            }
            else if(s.charAt(i) == ')'){
                int prevSign = stack.pop();
                res = prevSign * res;
                int prevAns = stack.pop();
                res += prevAns;
            }
        }
        return res;
    }
}