from grid import Grid
from window import Window


class Application:
    def __init__(self):
        self.N = 50 # num cells in each row/column
        self.SIZE = 12 # cell width/height in pixels
        self.grid = Grid(self.N)
        self.window = Window(self.N, self.SIZE)
        # Draw initial state of grid to canvas.
        for x in range(self.N):
            for y in range(self.N):
                cell_id = self._cell_id(x, y)
                is_alive = self.grid.cell(x, y)
                self.window.update_cell(cell_id, is_alive)

    def update(self):
        # Use the grid's changes to update the canvas.
        for cell, is_alive in self.grid.update():
            cell_id = self._cell_id(cell[0], cell[1])
            self.window.update_cell(cell_id, is_alive)
        self.window.root.after(250, self.update)
    
    def _cell_id(self, x, y):
        # Return the cell's id on the window's canvas.
        return (x * self.N) + y + 1


def main():
    app = Application()
    app.update()
    app.window.root.mainloop() # Why does this need to be here?!


main()