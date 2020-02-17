import random
import h_cost
import queen8_without_sideway

def r_main():
    N = int(input("Enter the value of n for a nXn square box: "))
    if (N < 4):
        print("enter input value greater than 3")
        r_main()

    steps_store=[]
    avg_board=[]
    for i in range(0,1000):
        success_no = 0
        step = 0
        l=0
        while success_no !=1:
            board = []
            for j in range(N):
                board.append(random.randint(0, N - 1))
            print("boar number=",l)
            l = l + 1
            h_cost.print_board(board, N)
            h = h_cost.heuristic(board)
            print("value of h=", h, "\n")
            while h != 0:
                newboard = queen8_without_sideway.steep_hill(board)
                hnew = h_cost.heuristic(newboard)
                if (h == hnew):
                    print("failure", "\n")
                    break
                h = hnew
                h_cost.print_board(board, N)

                print("value of h=", h, "\n")
                if (h == 0):
                    print("success", "\n")
                    success_no=1
                    steps_store.append(step)
                    avg_board.append(l)
                step = step + 1


    print("Average number of iterations",sum(avg_board)/len(avg_board))
    print("Average number of steps for success",sum(steps_store) / len(steps_store))




