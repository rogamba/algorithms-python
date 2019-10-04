""" Given a NxN matrix, get the submatrix with the largest 
    possible sum

    Solution (tree like strucure):
                        N x N
        ---
        N-(fist row) x N     
        N x N-(fist column)  
        N-(last row) x N     
        N x N-(last column)                

"""
import sys

board = [
    [-60, 2, 3, 4],
    [2, 3, 4, 5],
    [3, 4, 5, 6],
    [4, 5, 6, 7],
]

def get_adjacent_matrices(matrix):
    # Get the 4 adjacent matrices
    m1 = matrix[1:]
    m2 = matrix[:-1]
    m3 = [ row[1:] for row in matrix if row[1:] ]
    m4 = [ row[:-1] for row in matrix if row[:-1] ]
    resp = []
    if m1: resp.append(m1)
    if m2: resp.append(m2)
    if m3: resp.append(m3)
    if m4: resp.append(m4)
    return resp

def calculate_sum(matrix):
    # Calculate sum
    return sum([sum(row) for row in matrix])

def get_max_sum(matrix):
    max_matrix = []
    max_sum = 0

    def recurse_branches(_matrix):
        nonlocal max_sum, max_matrix
        current_sum = calculate_sum(_matrix)
        if current_sum > max_sum:
            max_sum = calculate_sum(_matrix)
            max_matrix = _matrix
        adjacent = get_adjacent_matrices(_matrix)
        if not adjacent:
            return
        for adj in adjacent:
            recurse_branches(adj)

    recurse_branches(matrix)
    return max_matrix


if __name__ == '__main__':
    from pprint import pprint
    matrix = get_max_sum(board)
    pprint(matrix)