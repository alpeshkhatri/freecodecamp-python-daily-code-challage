def live_or_die(current_life,live_neighbor):
    die = 0
    live = 1
    if current_life == live:
        if live_neighbor < 2 or live_neighbor > 3:
            return die
        else :
            return live
    if current_life == die :
        if live_neighbor == 3 :
            return live
        else:
            return die

def game_of_life(grid):
    check_idx = {0 :[0,1], 1: [-1,0,1], 2:[-1,0]}
    ret = []
    size = len(grid)
    for ridx,row in enumerate(grid):
        ret.append([])n
        for cidx,col in enumerate(row) :
            corner = ridx in [0,size-1] and cidx in [0,size-1]
            edge = False
            if not corner :
                edge   = ridx in [0,size-1] or cidx in [0,size-1]
            print(f'{corner=} {edge=}')
            current_cell_life = grid[ridx][cidx]
            live_neighbors = 0 - current_cell_life
            for r in check_idx[ridx] :
                for c in check_idx[cidx] :
                    live_neighbors += grid[ridx+r][cidx+c]
                    ## print(5,5,r,c,live_neighbors,grid[r][c])
            ret[ridx].append(live_or_die(current_cell_life,live_neighbors))
            ##print(ridx,cidx,current_cell_life,live_neighbors)
    print(ret)
    return ret

## alternative.
def game_of_life(matrix):
    if not matrix or len(matrix) == 0:
        return matrix
    
    rows = len(matrix)
    cols = len(matrix[0])
    next_state = [[0] * cols for _ in range(rows)]
    
    def count_neighbors(r, c):
        """Count live neighbors for a cell at (r, c)"""
        count = 0
        for dr in range(-1, 2):
            for dc in range(-1, 2):
                if dr == 0 and dc == 0:
                    continue  # Skip the cell itself
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    count += matrix[nr][nc]
        return count
    
    # Apply rules to each cell
    for r in range(rows):
        for c in range(cols):
            neighbors = count_neighbors(r, c)
            is_alive = matrix[r][c] == 1
            
            if is_alive:
                # Live cell with 2 or 3 neighbors survives
                next_state[r][c] = 1 if neighbors in [2, 3] else 0
            else:
                # Dead cell with exactly 3 neighbors becomes alive
                next_state[r][c] = 1 if neighbors == 3 else 0
    
    return next_state



if __name__ == '__main__' :
    game_of_life([[0, 1, 0], [0, 1, 1], [1, 1, 0]])

# [0, 1, 0]
# [0, 1, 1]
# [1, 1, 0]