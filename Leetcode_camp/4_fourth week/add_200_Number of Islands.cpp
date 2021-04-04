class Solution {
public:
    int numIslands(vector<vector<char>>& grid) {
        //DFS
        int answer=0;
        for(int row=0; row<grid.size();++row){
            for(int col=0; col<grid[row].size();++col){
                if(grid[row][col]=='1'){
                    ++answer;
                    dfs(grid,row,col);
                }
            }    
        }    
        return answer;
    }
    
    void dfs(vector<vector<char>>& g, int r, int c){
        int num_r = g.size(), num_c = g[0].size();
        
        g[r][c] = '0';
        
        if((r-1 >=0) && (g[r-1][c] == '1')){
            dfs(g,r-1,c);
        }
        if((r+1 < num_r) && (g[r+1][c] == '1')){
            dfs(g,r+1,c);
        }
        if((c-1 >=0) && (g[r][c-1] == '1')){
            dfs(g,r,c-1);
        }
        if((c+1 < num_c) && (g[r][c+1] == '1')){
            dfs(g,r,c+1);
        }
        
    }
    
};