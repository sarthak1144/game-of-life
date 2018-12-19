import copy
import random


class Grid:
    def __init__(self, n=10):
        # Create a NxN grid of dead cells.
        # True == ALIVE, False == DEAD
        self._cells = []
        for x in range(n):
            self._cells.append([])
            for _ in range(n):
                # Each cells has a 50% chance to be alive initially.
                self._cells[x].append(random.choice([True, False]))
    
    def cell(self, x, y):
        # Return the state of the cell at (x, y).
        return self._cells[x][y]

    def update(self):
        # Update the state of each cell based on the rules.
        # Return a list of changed cells' positions and new values.
        # TODO: Can this methed be refactored and cleaned up?
        new_cells = copy.deepcopy(self._cells)
        changes = []

        n = len(self._cells)
        for x in range(n):
            for y in range(n):
                lives = self._count_live_neighbors(x, y, n)
                if (self._cells[x][y]):
                    if (lives < 2) or (lives > 3):
                        new_cells[x][y] = False
                        changes.append([(x, y), new_cells[x][y]])
                elif (lives == 3):
                    new_cells[x][y] = True
                    changes.append([(x, y), new_cells[x][y]])
        
        self._cells = new_cells
        return changes

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
