def rock_paper_scissors(p1_score, p2_score):
    p1 = input("Scissors, Paper, Rock! ").lower()
    p2 = input("Scissors, Paper, Rock! ").lower()
    advantages = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if p1 == p2:
        draw_game(p1_score, p2_score)
    elif advantages[p1] == p2:
        win_game("P1", p1_score, p2_score)
    else:
        win_game("P2", p1_score, p2_score)


def draw_game(p1_score, p2_score):
    draw = input("DRAW! Try again? y/n ").lower()
    if draw == "y":
        return rock_paper_scissors(p1_score, p2_score)
    elif draw == "n":
        print("Good Game!")
        scoring(p1_score, p2_score)
    else:
        print(ValueError)


def win_game(msg, p1_score, p2_score):
    if msg == "P1":
        p1_score += 1
    else:
        p2_score += 1
    win = input(msg + " wins! Try again? y/n ").lower()
    if win == "y":
        return rock_paper_scissors(p1_score, p2_score)
    elif win == "n":
        print("Good Game!")
        scoring(p1_score, p2_score)
    else:
        return ValueError


def scoring(p1_score, p2_score):
    print("P1: " + str(p1_score) + "\nP2: " + str(p2_score))
    if p1_score == p2_score:
        print("DRAW!")
    elif p1_score > p2_score:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")


rock_paper_scissors(0, 0)
