from solution import Solution


def main():
    grid = Solution("test_inp.game")
    flag = True
    grid.display()
    while flag:
        flag = grid.solve()
    grid.display()

    if grid.solved():
        print "Congrats!!! Sudoku solved"

if __name__ == '__main__':
    main()
