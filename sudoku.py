def valid_move(grid, row, col, num):
    #kiem tra tren hang ko trung
    for x in range(9):
        if grid[row][x] == num:
            return False

    #kiem tra tren cot ko trung
    for x in range(9):
        if grid[x][col] == num:
            return False

    # Kiểm tra theo từng ô 3x3 nhỏ
    corner_row = row - row % 3
    corner_col = col - col % 3
    for x in range(3):
        for y in range(3):
            if grid[corner_row + x][corner_col + y] == num:
                return False
    
    return True

def solve(grid, row, col):
    if col == 9:
        if row == 8:
            return True
        row += 1
        col = 0

    if grid[row][col] > 0:
        return solve(grid, row, col + 1)
    
    for number in range(1,10):
        if valid_move(grid, row, col, number):
            grid[row][col] = number

            if solve(grid, row, col + 1):
                return True
        
        grid[row][col] = 0
    return False

grid = [[7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]]

if solve(grid, 0, 0):
    for i in range(9):
        for j in range(9):
            print(grid[i][j], end=" ")
        print()
else:
    print("Không giải được Sukudo này")    
