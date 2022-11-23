class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        for (int i = 0; i < 9; ++i) {
            bool row[9] = {false}, col[9] = {false}, cub[9] = {false};
            int rowIdx = 3*(i/3), colIdx = 3*(i%3);
            for (int j = 0; j < 9; ++j) {
                if (board[i][j] != '.') {
                    if (row[board[i][j]-'1']) return false;
                    row[board[i][j]-'1'] = true;
                }
                if (board[j][i] != '.') {
                    if (col[board[j][i]-'1']) return false;
                    col[board[j][i]-'1'] = true;
                }

                if (board[rowIdx+j/3][colIdx+j%3] != '.') {
                    if (cub[board[rowIdx+j/3][colIdx+j%3]-'1']) return false;
                    cub[board[rowIdx+j/3][colIdx+j%3]-'1'] = true;
                }

            }
        }
        return true;
    }
};