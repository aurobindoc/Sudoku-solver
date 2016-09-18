from cell import Cell
import re


class Solution:
    def __init__(self, inp_file):
        # Initialise the sudoku grid from input file
        f = open(inp_file)
        row = 0
        self.cells = [0] * 81

        while 1:
            line = f.readline()
            if not line:
                break
            if line[0] in '#-':
                continue

            line = re.sub("\|", "", line)
            line = re.sub(" ", "", line)

            for col in range(9):
                cell_id = row * 9 + col
                cell = Cell(cell_id)
                char = line[col]
                try:
                    cell.value = int(char)
                    cell.possible_values = set([cell.value])
                except:
                    pass

                self.cells[cell_id] = cell
            row += 1

        if row != 9:
            raise "Exception: less than 9 rows!!!!"

    def solved(self):
        # returns True if sudoku is solved
        return len(filter(lambda x: x.value == 0, self.cells)) == 0

    def display(self):
        # Display the sudoku Grid wise
        out = ""
        for row in range(9):
            if row == 3 or row == 6:
                out += "------+-------+------\n"
            for col in range(9):
                if col == 3 or col == 6:
                    out += "| "
                cell = self.cells[row * 9 + col]
                what = cell.value or "."
                out += "%s " % what
            out += '\n'
        print out

    def solve(self):
        # Iterates and solves sudoku until no more changes could be made
        if_modified = False
        for c in self.cells:
            c.update_possible_values(self.cells)
            if c.value == 0 and len(c.possible_values) == 1:
                c.value = c.possible_values.pop()
                c.possible_values.add(c.value)
                if_modified = True
        return if_modified
