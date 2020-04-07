import random
import Draw


def probabilistic_blocks(rows, cols):
    b = set()
    for y in range(rows):
        for x in range(cols):
            count = 1
            total = 0
            for i in range(3):
                for j in range(3):
                    shift_y = y + (i - 1)
                    shift_x = x + (j - 1)
                    if 0 <= shift_x < cols and 0 <= shift_y < rows:
                        count = count + 1 if (shift_y, shift_x) in b else count
                        total = total + 1
            p = random.uniform(0, total)
            if p <= count: b.add((y, x))
    return b


class Grid:
    def __init__(self, rows, cols, start, finish):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.finish = finish
        self.current = start
        #self.arena = [[0]*cols for i in range(rows)]
        self.blocks = probabilistic_blocks(rows, cols)

    def get_next(self):
        pw = []
        for i in range(3):
            for j in range(3):
                shift_y = self.current[0] + (i-1)
                shift_x = self.current[1] + (j-1)
                if 0 <= shift_x < self.cols and 0 <= shift_y < self.rows and not (shift_x == self.current[1] and shift_y == self.current[0]):
                    if (shift_y, shift_x) not in self.blocks:
                        pw.append((shift_y, shift_x))
        return pw


def test():
    g = Grid(15,15, (3,0), (3,6))
    pos_list = [g.current]
    for i in range(20):
        g.current = random.choice(g.get_next())
        pos_list.append(g.current)
    print(pos_list)
    ani = Draw.Animate(g)
    ani.show(pos_list)


test()
