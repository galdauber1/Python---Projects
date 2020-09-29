

def print_to_n(n):
    """print numbers up to n"""
    if n > 0:
        print_to_n(n-1)
        print(n)

def print_reversed(n):
    """print numbers from n to 1"""
    if n < 1:
        return
    print(n)
    print_reversed(n-1)


def is_prime(n):
    """this func return true if the num is prime"""
    if n< 2:
        return False
    if n==2:
        return True
    if has_divisor_smaller_then(n,n-1):
        return True
    if not has_divisor_smaller_then(n,n):
        return False



def has_divisor_smaller_then(n,i):
    """"this func return true if i is the smallest divisor except 1"""
    if i <= 2:
        return True
    if n%i == 0:
        return False
    else:
        return has_divisor_smaller_then(n,i-1)


def factorial(n):
    """factorial func"""
    if n == 0:
        return 1
    return n*factorial(n-1)


def exp_n_x(n, x):
    """this func calculate the exponential sum"""
    if n == 0:
        return 1
    return (x**n)/factorial(n) + exp_n_x(n-1, x)



def play_hanoi(hanoi, n, src, dest, temp):
    """hanoi game solution"""
    if n >0:
        play_hanoi(hanoi, n - 1, src, temp, dest)
        hanoi.move(src, dest)
        play_hanoi(hanoi, n - 1, temp, dest, src)


def print_sequences_helper(char_list, n, comb_string=''):
    """this func print all possible permutation with repetition """
    if n == 0:
        return None
    if len(comb_string) == n:
        print(comb_string)
    else:
        for char in char_list:
            print_sequences_helper(char_list, n, comb_string+char)


def print_sequences(char_list,n):
    """this func print all possible permutation with repetition """
    print_sequences_helper(char_list, n)
    if n==0:
        return None




def print_no_repetition_sequences_helper(char_list, n, comb_string=''):
    """this func print all possible permutation without repetition """
    if n == 0:
        return None
    if len(comb_string) == n:
        print(comb_string)
    else:
        for char in char_list:
            if char not in comb_string:
                print_no_repetition_sequences_helper(char_list, n, comb_string+char)


def print_no_repetition_sequences(char_list,n):
    """this func print all possible permutation without repetition """
    print_no_repetition_sequences_helper(char_list,n)
    if n==0:
        return None


def parentheses_helper(output, open, close, n,res_list):
    """this func print all valid parentheses permutation"""
    res_list = res_list
    if open == n and close == n:  # if the num of open/close are n print
        res_list.append(output)
    else:
        if open < n:  # if ( smaller the n
            parentheses_helper(output+'(', open+1, close, n,res_list)
        if close < open:  # if ( smaller the n
            parentheses_helper(output+')', open, close+1, n,res_list)
    return res_list

def parentheses(n):
    """call the parentheses_helper func """
    return (parentheses_helper('', 0, 0, n,[]))


def up_and_right(n, k):
    """this func call the up_and_right_helper func """
    up_and_right_helper('', 0, 0, n, k)


def up_and_right_helper(output, up, right, n, k):
    """print all route to n,k permutations"""
    if n == 0 and k==0:
        return None
    if up == n and right == k:
        print(output)
    else:
        if up < n:
            up_and_right_helper(output + 'r', up + 1, right, n, k)
        if right < k:
            up_and_right_helper(output + 'u', up , right + 1, n, k)


def flood_fill(image,start):
    """flood_fill"""
    if image[start[0]][start[1]] == '.':
        image[start[0]][start[1]] = '*'
        if start[0] > 0:
            flood_fill(image,(start[0]-1,start[1]))
        if start[0] < len(image[0]):
            flood_fill(image, (start[0]+1, start[1]))
        if start[1] > 0 :
            flood_fill(image,(start[0],start[1]-1))
        if start[1] < len(image)-1:
                flood_fill(image, (start[0], start[1] + 1))



