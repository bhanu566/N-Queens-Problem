#Hill climbing algorithm for 8 queen problem
#Author:bhanu prakash reddy chennam
#       Sathabdhi Reddy

import random_restart_nosideways
import random_restart_sidewaymoves
import queen8_with_sidemoves
import queen8_without_sideway


def main():
    N=int(input("\n\nEnter 1 for 8 queen problem without sideway moves"
                "\nEnter 2 for 8 queen problem with sideway moves\n"
                "Enter 3 for random restart without sideway moves\n"
                "Enter 4 for random restart with sideway moves\n"
                "Enter 5 to exit\n"
                "Please select the options: "))


    if N==1:
        queen8_without_sideway.q2_main()
    elif N==2:
        queen8_with_sidemoves.q1_main()
    elif N==3:
        random_restart_nosideways.r_main()
    elif N==4:
        random_restart_sidewaymoves.r2_main()
    elif N==5:
        return
    else:
        print("Enter correct input\n")

    main()






if __name__ == "__main__":
    main()