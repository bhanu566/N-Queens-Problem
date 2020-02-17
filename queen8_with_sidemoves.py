import random
import h_cost

previous_moves=[]
flag=0
def steep_hill(board):
    global previous_moves
    global flag
    moves = {}
    for col in range(len(board)):
        for row in range(len(board)):
            if board[col] == row:
                continue
            board_copy = list(board)
            board_copy[col] = row
            moves[(col, row)] = h_cost.heuristic(board_copy)

    best_moves = []
    h_old = h_cost.heuristic(board)
    for k, v in moves.items():
        if v < h_old:
            h_old = v

    for k, v in moves.items():
        if v == h_old:
            best_moves.append(k)

    if len(best_moves)==0:
        flag=1
        return board
    if len(best_moves) > 0:
        pick = random.randint(0, len(best_moves) - 1)
        col = best_moves[pick][0]
        row = best_moves[pick][1]
        board[col] = row

    return board


def q1_main():
    global previous_moves
    global flag
    N=int(input("Enter the value of n for a nXn square box: "))
    if(N<4):
        print("enter input value greater than 3")
        q1_main()
    success_no=0
    failure_no=0
    step_succeed=[]
    step_fail=[]
    for i in range(0,1000):
        step=0
        flag=0
        board=[]
        print("board number = ",i+1)
        for j in range(N):
            board.append(random.randint(0, N-1))
        # board=random.sample(range(0,N),N)
        h_cost.print_board(board,N)
        h=h_cost.heuristic(board)
        print("value of h=",h,"\n")
        l=0
        while h!=0:
            newboard=steep_hill(board)

            hnew=h_cost.heuristic(newboard)
            step = step + 1
            if step == 100 or flag==1:
                failure_no = failure_no + 1
                print("failure", "\n")
                step_fail.append(step)
                break

            h=hnew
            h_cost.print_board(board, N)

            print("value of h=",h,"\n")

            if (h == 0):
                print("success", "\n")
                success_no = success_no + 1
                step_succeed.append(step)


    print("Total success percentage=",success_no/10,"%")
    print("Total failure percentage=",failure_no/10,"%")
    print("Average of steps when succeed",sum(step_succeed) / len(step_succeed))
    print("Average of steps when fail",sum(step_fail) / len(step_fail))


