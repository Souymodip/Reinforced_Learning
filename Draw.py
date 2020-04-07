from tkinter import *
from PIL import Image
from PIL import ImageTk


def draw_running_man(cor_x, cor_y, photo, canvas):
    canvas.create_image(cor_y*40+1+18, cor_x*40+1+18, image=photo)


def draw_fill_box(cor_x, cor_y, canvas):
    canvas.create_rectangle(cor_y*40+1, cor_x*40+1, cor_y*40+39, cor_x*40+39, outline="blue", fill="blue")


def draw_blocks(cor_x, cor_y, canvas):
    canvas.create_rectangle(cor_y*40+1, cor_x*40+1, cor_y*40+39, cor_x*40+39, outline="black", fill="black")


def erase_fill_box(cor_x, cor_y, canvas):
    canvas.create_rectangle(cor_y*40+1, cor_x*40+1, cor_y*40+39, cor_x*40+39, outline="white", fill="white")


def draw_grid(rows, cols, blocks, canvas):
    start_x = 0
    start_y = 0
    for i in range(rows+1):
        canvas.create_line(start_x, start_y+i*40, start_x + cols*40, start_y + i*40)
    for i in range(cols+1):
        canvas.create_line(start_x + i*40, start_y, start_x + i*40, start_y + rows*40)
    for b in blocks:
        draw_blocks(b[0], b[1], canvas)


class Animate:
    def __init__(self, grid):
        self.rows = grid.rows
        self.cols = grid.cols
        self.blocks = grid.blocks

    def show(self, pos_list):
        root = Tk()
        root.title("Time Delayed")
        cw = 800  # canvas width
        ch = 650  # canvas height
        canvas = Canvas(root, width=cw, height=ch, background="white")
        canvas.grid(row=0, column=0)
        draw_grid(self.rows, self.cols, self.blocks, canvas)
        photo = PhotoImage(file=r"C:\Users\souymo\PycharmProjects\Reinforced_Learning\run_right_37.png")
        #draw_running_man(2,2, photo, canvas)

        cycle_period = 1000  # time between fresh positions of the ball
        for pos in pos_list:
            print(pos)
            draw_running_man(pos[0], pos[1], photo, canvas)
            canvas.update()
            canvas.after(cycle_period)
            erase_fill_box(pos[0], pos[1], canvas)
        draw_fill_box(pos_list[-1][0], pos_list[-1][1], canvas)
        root.mainloop()
