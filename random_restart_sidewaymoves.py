import random
import h_cost
import queen8_with_sidemoves
previous_moves=[]
flag=0



def r2_main():
    global previous_moves
    global flag
    N = int(input("Enter the value of n for a nXn square box: "))
    if (N < 4):
        print("enter input value greater than 3")
        r2_main()
    steps_store=[]
    avg_board=[]
    for i in range(0, 1000):

        success_no = 0
        l=0

        while success_no != 1:
            global flag
            step = 0
            flag=0
            board = []
            for j in range(N):
                board.append(random.randint(0, N - 1))
            h_cost.print_board(board, N)
            print("boar number=", l)
            l = l + 1
            h = h_cost.heuristic(board)
            print("value of h=", h, "\n")
            while h != 0:
                newboard = queen8_with_sidemoves.steep_hill(board)

                hnew = h_cost.heuristic(newboard)
                print("value of flag ",flag)
                if step == 100 or flag == 1:
                    print("failure", "\n")
                    break

                h = hnew
                h_cost.print_board(board, N)
                # print(board)

                print("value of h=", h, "\n")
                step = step + 1
                if (h == 0):
                    print("success", "\n")
                    success_no = 1
                    steps_store.append(step)
                    avg_board.append(l)
                step = step + 1

    print("Average number of iterations",sum(avg_board)/len(avg_board))
    print("Average number of steps for success",sum(steps_store) / len(steps_store))



