

def illegal_row_placement(number,board,row):
    """check if number already in the row if yes return false"""
    for i in range(len(board[row])):
        if board[row][i] == number:
            return False
    return True


def illegal_col_placement(number,board,col):
    """check if number already in the col if yes return false"""
    for i in range(len(board)):
        if board[i][col]== number:
            return False
    return True


def illegal_square_placement(number,board,col,row):
    """check if the number is in the n^0.5Xn^0.5 square return false"""
    col_pointer = col - col % (int(len(board)**0.5))
    row_pointer = row - row % (int(len(board)**0.5))
    for i in range(int(len(board)**0.5)):
        for j in range(int(len(board)**0.5)):
            if board[i+row_pointer][j+col_pointer]== number:
                return False
    return True


def illegal_placement(number,board,col,row):
    """check if the placement of number is valid and return true or false"""
    return illegal_row_placement(number,board,row) and \
           illegal_col_placement(number,board,col) and \
        illegal_square_placement(number,board,col,row)


def find_empty(board, empty):
    """find the first empty cell and set row and col and true will returned
    else return false  empty is a list"""
    for row in range(len(board)):
        for col in range(len(board)):
            if board[row][col] == 0:
                empty[0] = row
                empty[1] = col
                return True
    return False


def solve_sudoku(board):
    """this func try to fill al empty cells with legal number
    by using backtracking
    """
    empty = [0, 0]
    if not find_empty(board, empty):  # if there are no empty cells return TRUE
        return True
    row = empty[0]  # row of the empty cell
    col = empty[1]  # col of the empty cell
    for number in range(1, len(board)+1):  # numbers from 1 up to n
        if illegal_placement(number, board, col, row):  # if the assign islegal
            board[row][col] = number
            if solve_sudoku(board):
                return True
            board[row][col] = 0  # undo
    return False


def print_k_subsets(n,k):
    """Given a number n, and a number k <= n, print lists
of 0,…,n-1 in size exactly k."""
    if k <= n and k != 0:
        cur_set = [False] * n
        print_k_subsets_helper(cur_set, k, 0, 0)


def print_k_subsets_helper(cur_set, k, index, picked):
    """helper func for print_k_subsets(n,k) """
    # Base: we picked out k items.
    if k == picked:
        sub_list = []
        for (idx, in_cur_set) in enumerate(cur_set):
            if in_cur_set:
                sub_list.append(idx)
        print(sub_list)
        return
    # If we reached the end of the list, backtrack.
    if index == len(cur_set):
        return
    cur_set[index] = True
    print_k_subsets_helper(cur_set, k, index + 1, picked + 1)
    cur_set[index] = False
    print_k_subsets_helper(cur_set, k, index + 1, picked)





def fill_k_subsets(n,k,lst):
    """Given a number n, and a number k <= n, print list of list
of 0,…,n-1 in size exactly k."""
    if k <= n:
        cur_set = [False] * n
        fill_k_subsets_helper(cur_set, k, 0, 0, lst)
    print(lst)


def fill_k_subsets_helper(cur_set, k, index, picked,lst):
    """helper function for fill_k_subsets(n,k,lst): """
    if k == picked:
        sub_list = []
        for (idx, in_cur_set) in enumerate(cur_set):
            if in_cur_set:
                sub_list.append(idx)
        lst.append(sub_list)
        return
    if index == len(cur_set):
        return
    cur_set[index] = True
    fill_k_subsets_helper(cur_set, k, index + 1, picked + 1, lst)
    cur_set[index] = False
    fill_k_subsets_helper(cur_set, k, index + 1, picked, lst)



def return_k_subsets_helper(n, k, picked):
    """helper function for  return_k_subsets(n, k):"""
    if k == picked:
        return [[]]

    res = []
    for i in range(n):
        lists_with_i = return_k_subsets_helper(i, k, picked + 1)
        for lst in lists_with_i:
            lst.append(i)
        res += lists_with_i

    return res


def return_k_subsets(n, k):
    """Given a number n, and a number k <= n, print list of list
of 0,…,n-1 in size exactly k without using lists as arguments"""
    if k <= n:
        return return_k_subsets_helper(n, k, 0)



