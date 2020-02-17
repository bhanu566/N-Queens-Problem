import numpy as np

def heuristic(board_n):
    h = 0
    for i in range(len(board_n)):
        for j in range(i + 1, len(board_n)):
            if board_n[i] == board_n[j]:
                h += 1
            offset = j - i
            if (board_n[i] == board_n[j] - offset) or (board_n[i] == board_n[j] + offset):
                h += 1
    return h


def print_board(board_n, N):
    board_n = np.array(board_n)
    board_n = N - 1 - board_n
    l = []
    for i, j in enumerate(board_n):
        l.append([i, j])

    for i in range(0, N):
        for j in range(0, N):
            if [j, i] in l:
                print("X ", end="")
            else:
                print("O ", end="")
        print(end="\n")