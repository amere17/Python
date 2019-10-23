import random
import os
import sys
import time

# --------------- Sudoku solver ---------------
# main board of the soduko
boardS = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# temp board to mark the index that the user filled
flagS = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0, 0, 0]]

# set of numbers, the max length of this set is 9
number = {0}


# solve the sudoku board
def solve_sudoku(cell):
    global boardS
    global number
    i = 1
    sys.setrecursionlimit(300000)
    start = square_f(cell)
    while True:
        randNum = i
        if i != 9:
            i += 1
        number.add(randNum)
        # check if the value match in this row, column and square. and the index is empty ( equal 0)
        if check_row(cell, randNum) and check_col(cell, randNum) and check_sqr(start, randNum) and empty_index(cell):
            index_fill(cell, randNum)
            cell = cell2fill()
            solve_sudoku(cell)
        # if none of the numbers between 1-9 match in any index
        elif len(number) == 9 and 0 in boardS[int(cell[0])]:
            if empty_index(cell):
                again(cell)
            cell = cell2fill()
            number.clear()
            solve_sudoku(cell)

        if valid_s():
            return True
    return False


# check again the board if the index can not by fill
def again(cell):
    global number
    for j in range(9):
        i = 1
        cell = cell[0] + str(j)
        start = square_f(cell)
        while True:
            randNum = i
            if i <= 9:
                i += 1
            else:
                break
            number.add(randNum)
            if check_row(cell, randNum) and check_col(cell, randNum) and check_sqr(start, randNum) and empty_index(
                    cell):
                if boardS[int(cell[0])][int(cell[1])] != randNum:
                    boardS[int(cell[0])][int(cell[1])] = randNum
                    break


# find the square
def square_f(cell):
    row = int(cell[0])
    col = int(cell[1])
    if row < 3:
        start = "0"
    elif 3 <= row < 6:
        start = "3"
    else:
        start = "6"
    if col < 3:
        start += "0"
    elif 3 <= col < 6:
        start += "3"
    else:
        start += "6"
    return start


# solve each index individually
def index_fill(cell, num):
    global number
    global boardS
    number.clear()
    boardS[int(cell[0])][int(cell[1])] = num


# find a cell to fill
def cell2fill():
    cell = '00'
    for i in range(len(boardS[0])):
        for j in range(len(boardS[1])):
            if boardS[i][j] == 0:
                cell = str(i) + str(j)
                return cell
    return cell


# find index not filled by the user
def empty_index(cell):
    if flagS[int(cell[0])][int(cell[1])] == 0:
        return True
    else:
        return False


# check valid Raw
def check_row(cell, num):
    for i in range(len(boardS[0])):
        if num == boardS[int(cell[0])][i] and i != int(cell[1]):
            return False
    return True


# check valid column
def check_col(cell, num):
    for i in range(len(boardS[0])):
        if num == boardS[i][int(cell[1])] and i != int(cell[0]):
            return False
    return True


# check valid square
def check_sqr(sqr, num):
    counter = 0
    i = int(sqr[0])
    j = int(sqr[1])
    m = i + 3
    k = j + 3
    for i in range(i, m):
        for j in range(j, k):
            if num == boardS[i][j]:
                counter += 1
        j = k - 3
    if counter >= 1:
        return False
    return True


# input data to the board
def input_data():
    global boardS
    global flagS
    values = "y"
    print("________________________________________")
    print("_____ fill Your sudoku to solve it _____")
    print("________________________________________")
    while values != "n":
        while True:
            row = int(input("choose a row (row: 0-8) "))
            col = int(input("choose a column (col: 0-8) "))
            num = int(input("choose a value (value: 1-9) "))
            if 0 <= row <= 8 and 0 <= col <= 8 and 0 < num < 10:
                break
            else:
                print("__________________________________________________________________________")
                print("_______ Invalid input!. Please try a new input (row, col and value) ______")
                print("__________________________________________________________________________")
        boardS[row][col] = num
        flagS[row][col] = -1
        values = input("more Values? y/n: ")

    while True:
        cell = cell2fill()
        if solve_sudoku(cell):
            break
    time.sleep(5)
    print_board()
    return


# check valid sudoku
def valid_s():
    sumV = 0
    for k in range(9):
        for m in range(9):
            sumV += int(boardS[k][m])
    if sumV == 405:
        return True
    else:
        return False


# print Sudoku Board
def print_board():
    for i in range(len(boardS[0])):
        print(boardS[i])
    print("____________________________________")
    print("____________________________________")


# reset the board
def reset_board():
    global flagS, boardS
    for i in range(len(boardS[0])):
        for j in range(len(boardS[1])):
            boardS[i][j] = 0
            flagS[i][j] = 0


# function to start the program
def start_SS():
    while True:
        reset_board()
        input_data()
        newSS = input(" do you want to solve another sudoku board? y/n: ")
        if newSS == 'n':
            break


start_SS()
