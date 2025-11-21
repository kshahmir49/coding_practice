def check_rows(sudoku):
    for i in sudoku:
        for j in range(len(i)-1):
            for k in range(j+1,len(i)):
                if i[j] == i[k] and i[j]!=".":
                    return False
    return True

def check_columns(sudoku):
    for k in range(len(sudoku)):
        ll = []
        for i in sudoku:
            ll.append(i[k])
        for j in range(len(ll)-1):
            for k in range(j+1,len(ll)):
                if ll[j] == ll[k] and ll[j]!=".":
                    return False
    return True

def check_cubes(sudoku):
    ll = []
    for i in range(0,9,3):
        for j in range(0,9,3):
            for h in range(i,i+3):
                for k in range(j,j+3):
                    ll.append(sudoku[h][k])
            for a in range(8):
                for b in range(a+1,9):
                    if ll[a] == ll[b] and ll[b]!=".":
                        return False
            ll = []
    return True

def check_sudoku(sudoku):
    return check_columns(sudoku) and check_cubes(sudoku) and check_rows(sudoku)