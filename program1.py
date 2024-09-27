class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
    #function to perform dfs
       def dfs(grid,i,j,visited):
        if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]) or grid[i][j]=='W' or visited[i][j]:
           return 
        visited[i][j]=True
        #visited all the connected land

        dfs(grid,i-1,j,visited)
        dfs(grid,i+1,j,visited)
        dfs(grid,i,j-1,visited)
        dfs(grid,i,j+1,visited)

       if not grid:
          return 0
    
        rows,cols=len(grid),len(grid[0])
       
        visited=[[False for]]

                    
        return 0
