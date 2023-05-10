# task 15 - 2d lists
# code to count the number of mines adjacent to spaces in a grid

# function takes a 2d list of # mines and - spaces
def minesweeper(grid):

    # count rows and columns in the input grid
    rows, cols = len(grid), len(grid[0])
    
    # create new grid of 0s with the same dimensions as the input 
    counts = [[0 for i in range(cols)] for j in range(rows)]

    # possible adjacent compass positions
    directions = [[-1,-1], [-1, 0], [-1, 1],  # row above
                 [0,-1], [0 , 1],             # current row
                 [1,-1], [1, 0], [1, 1]]      # row below
    
    # loop through each row in input grid
    for i in range(rows):

        # loop through each column in input grid
        for j in range(cols):

            # current cell is marked as # if a mine
            if grid[i][j] == "#":
                counts[i][j] = "#"
                continue

            # loop through each adjacent compass direction
            for k in directions:

                # create index for next adjacent cell
                adjacent_row, adjacent_col = i + k[0], j + k[1]

                # row and column boundary check
                if 0 <= adjacent_row < rows and 0 <= adjacent_col < cols:

                    # increment count of current cell if a mine is adjacent
                    if grid[adjacent_row][adjacent_col] == "#":
                        counts[i][j] += 1

            # not strictly needed but matches expected output formatting
            # convert grid integers to strings
            if counts[i][j] != "#":
                counts[i][j] = str(counts[i][j])

    # return the grid with mine counts
    return counts

# custom grid of # mines and - spaces
input_grid = [["-", "-", "-", "#", "#"],
              ["-", "#", "-", "-", "-"],
              ["-", "-", "#", "-", "-"],
              ["-", "#", "#", "-", "-"],
              ["-", "-", "-", "-", "-"]]

# numerical grid output from function
count_grid = minesweeper(input_grid)

# print row by row to match example output
for row in count_grid:
    print(row)
