""" Given a board and, the starting position 
    of a character and the target position, 
    develop a method to get all possible paths
    from the starting position to the target
    position.

    0. Open spot
    1. Unavaiable spot (character can't pass)
    2. Goal

"""

board = [
    [1, 0, 1, 0, 1, 1],
    [1, 1, 1, 1, 1, 0],
    [1, 0, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0],
    [0, 0, 1, 1, 1, 0],
    [0, 1, 1, 1, 1, 1]
]

def get_adjacent(row, col):
    adj = []
    size_row, size_col = len(board), len(board[0])
    # Left
    if col > 0:
        adj.append((row,col-1))
    # Bottom
    if row < size_row-1:
        adj.append((row+1, col))
    # Right
    if col < size_col-1:
        adj.append((row, col+1))
    # Top
    if row > 0:
        adj.append((row-1,col))
    return adj


def get_paths(board, start, target):
    paths_to_goal = []
    target_row, target_col = target

    def step(position, path=set()):
        print(position)
        row, col = position
        # Get adjacent nodes
        adj = get_adjacent(*position)
        # Arrived to goal
        if row == target_row and col == target_col:
            print("---")
            paths_to_goal.append(path)
            return
        # Nowhere to move
        if len(adj) <= 0:
            return
        # Step
        for next_pos in adj:
            if board[next_pos[0]][next_pos[1]] == 0:
                continue
            if next_pos not in path:
                new_path = path.copy()
                new_path.add(next_pos)
                step(next_pos, path=new_path)

    # Recurse nodes
    step(start, path=set([start]))
    return paths_to_goal


if __name__ == '__main__':
    start = (0,0)
    target = (len(board)-1, len(board[0])-1)
    print("From {} to {}".format(start, target))
    paths = get_paths(board, start, target)
    print(len(paths))