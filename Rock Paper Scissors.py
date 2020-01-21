def rock_paper_scissors():
    p1 = input("Scissors, Paper, Rock! ").lower()
    p2 = input("Scissors, Paper, Rock! ").lower()
    advantages = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'scissors'}
    if p1 == p2:
        draw_game()
    elif advantages[p1] == p2:
        p1win_game()
    else:
        p2win_game()

def draw_game():
    draw = input("DRAW! Try again? y/n ").lower()
    if draw == "y":
        return rock_paper_scissors()
    elif draw == "n":
        print("Good Game!")
    else:
        print(ValueError)

def p1win_game():
    p1_win = input("P1 wins! Try again? y/n ").lower()
    if p1_win == "y":
        return rock_paper_scissors()
    elif p1_win == "n":
        print("Good Game!")
    else:
        return (ValueError)

def p2win_game():
    p2_win = input("P2 wins! Try again? y/n ").lower()
    if p2_win == "y":
        return rock_paper_scissors()
    elif p2_win == "n":
        print("Good Game!")
    else:
        return (ValueError)

rock_paper_scissors()