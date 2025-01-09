class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)
        
        visited=set()
        numofProvinces=0
        for start in range(len(isConnected)):
            if start not in visited:
                numofProvinces+=1
                dfs(start)
        return numofProvinces