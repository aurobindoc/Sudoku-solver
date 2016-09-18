class Cell:
    # Each cell in the Sudoku grid is defined by this class
    def __init__(self, cid):
        # Defining cell attributes
        self.cid = cid
        self.value = 0
        self.possible_values = set(range(1, 10))
        self.row = row = cid / 9
        self.col = col = cid % 9

        corner = ((row / 3) * 3) * 9 + ((col / 3) * 3)
        cell_box = range(corner, corner + 3) + range(corner + 9, corner + 12) + range(corner + 18, corner + 21)
        cell_box.remove(cid)
        cell_row = range(row * 9, row * 9 + 9)
        cell_row.remove(cid)
        cell_col = range(col, 81, 9)
        cell_col.remove(cid)

        # Defining attributes of friends of cell
        self.cell_box = tuple(cell_box)
        self.cell_row = tuple(cell_row)
        self.cell_col = tuple(cell_col)

    def update_possible_values(self, cells):
        # Based on friends cells eliminates possible values
        for friends in (self.cell_box, self.cell_row, self.cell_col):
            friends = map(lambda x: cells[x], friends)  # list of cell who are friend
            for f in friends:
                if f.value in self.possible_values:
                    self.possible_values.remove(f.value)




