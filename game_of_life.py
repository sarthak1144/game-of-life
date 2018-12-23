import tkinter

from grid import Grid


n = 50      # num cells in each row/column
size = 12   # cell width/height in pixels

job = None


def play():
    global job
    job = root.after(250, play)
    button.config(text="Pause", command=pause)
    for cell, is_alive in grid.update():
        id = (cell[0] * n) + cell[1] + 1
        if is_alive:
            canvas.itemconfig(id, fill="white")
        else:
            canvas.itemconfig(id, fill="black")


def pause():
    root.after_cancel(job)
    button.config(text="Play", command=play)


root = tkinter.Tk()
root.title("Conway's Game of Life")

grid = Grid(n)

canvas = tkinter.Canvas(root, width=n*size, height=n*size)
canvas.pack()

for x in range(n):
    for y in range(n):
        x0 = x * size
        y0 = y * size
        x1 = x0 + size
        y1 = y0 + size
        if grid.cell(x, y):
            color = "white"
        else:
            color = "black"
        canvas.create_rectangle(x0, y0, x1, y1, fill=color)

button = tkinter.Button(root, text="Play", command=play)
button.pack()

root.mainloop()