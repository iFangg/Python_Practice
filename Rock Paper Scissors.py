def rock_paper_scissors():
    p1 = input("Scissors, Paper, Rock! ")
    p1.lower()
    p2 = input("Scissors, Paper, Rock! ")
    p2.lower()
    if p1 == p2:
        draw = input("DRAW! Try again? y/n ")
        draw.lower()
        if draw =="y":
            return rock_paper_scissors()
        elif draw == "n":
            print()
        else:
            print(ValueError)

    elif p1 == "scissors" and p2 == "paper":
        p1_win = input("P1 wins! Try again? y/n ")
        p1_win.lower()
        if p1_win == "y":
            return rock_paper_scissors()
        elif p1_win =="n":
            print("Good Game!")
        else:
            return(ValueError)

    elif p1 == "scissors" and p2 == "rock":
        p2_win = input("P2 wins! Try again? y/n ")
        p2_win.lower()
        if p2_win == "y":
            return rock_paper_scissors()
        elif p2_win == "n":
            print("Good Game!")
        else:
            return(ValueError)

    elif p1 == "paper" and p2 == "scissors":
        p2_win = input("P2 wins! Try again? y/n ")
        p2_win.lower()
        if p2_win == "y":
            return rock_paper_scissors()
        elif p2_win == "n":
            print("Good Game!")
        else:
            return(ValueError)

    elif p1 == "paper" and p2 == "rock":
        p1_win = input("P1 wins! Try again? y/n ")
        p1_win.lower()
        if p1_win == "y":
            return rock_paper_scissors()
        elif p1_win == "n":
            print("Good Game!")
        else:
            return(ValueError)

    elif p1 == "rock" and p2 == "paper":
        p2_win = input("P2 wins! Try again? y/n ")
        p2_win.lower()
        if p2_win == "y":
            return rock_paper_scissors()
        elif p2_win == "n":
            print("Good Game!")
        else:
            return(ValueError)

    elif p1 == "rock" and p2 == "scissors":
        p1_win = input("P1 wins! Try again? y/n ")
        p1_win.lower()
        if p1_win == "y":
            return rock_paper_scissors()
        elif p1_win == "n":
            print("Good Game!")
        else:
            return(ValueError)

    else:
        print(ValueError)

rock_paper_scissors()
