import copy

class Grid:
    def __init__(self, n=10):
        # Create a NxN grid of dead cells.
        # True == ALIVE, False == DEAD
        self._cells = []
        for x in range(n):
            self._cells.append([])
            for _ in range(n):
                self._cells[x].append(False)

        # Add a blinker.
        self._cells[0][1] = True
        self._cells[1][1] = True
        self._cells[2][1] = True

    def update(self):
        # Update the state of each cell based on the rules.
        # TODO: Update this method to return a list of cells that have changed.
        new_cells = copy.deepcopy(self._cells)

        n = len(self._cells)
        for x in range(n):
            for y in range(n):
                lives = self._count_live_neighbors(x, y, n)
                if (self._cells[x][y]):
                    if (lives < 2) or (lives > 3):
                        new_cells[x][y] = False
                elif (lives == 3):
                    new_cells[x][y] = True
        
        self._cells = new_cells

    def _count_live_neighbors(self, x, y, n):
        top = (x - 1) % n
        left = (y - 1) % n
        right = (y + 1) % n
        bottom = (x + 1) % n

        lives = 0
        lives += int(self._cells[top][left])
        lives += int(self._cells[top][y])
        lives += int(self._cells[top][right])
        lives += int(self._cells[x][left])
        lives += int(self._cells[x][right])
        lives += int(self._cells[bottom][left])
        lives += int(self._cells[bottom][y])
        lives += int(self._cells[bottom][right])

        return lives
