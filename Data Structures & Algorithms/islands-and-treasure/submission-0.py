class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        cells = deque()
        visited = set()

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 0:
                    cells.append((row,col))
                    visited.add((row,col))

        val = 0

        def addRoom(row, col):
            if (row, col) in visited or not(0 <= row < rows and 0<= col < cols) or grid[row][col] == -1:
                return
            visited.add((row,col))
            cells.append((row,col))

        while cells:
            for i in range(len(cells)):
                row,col = cells.popleft()
                grid[row][col] = val

                addRoom(row + 1, col)
                addRoom(row - 1, col)
                addRoom(row,col + 1)
                addRoom(row,col - 1)
            val += 1


        

            

