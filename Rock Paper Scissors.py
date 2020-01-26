def rock_paper_scissors(p1_score, p2_score):
    p1 = input("Scissors, Paper, Rock! ").lower()
    p2 = input("Scissors, Paper, Rock! ").lower()
    advantages = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'scissors'}
    if p1 == p2:
        draw_game(p1_score, p2_score)
    elif advantages[p1] == p2:
        p1win_game(p1_score, p2_score)
    else:
        p2win_game(p1_score, p2_score)


def draw_game(p1_score, p2_score):
    draw = input("DRAW! Try again? y/n ").lower()
    if draw == "y":
        return rock_paper_scissors(p1_score, p2_score)
    elif draw == "n":
        print("Good Game!")
        scoring(p1_score, p2_score)
    else:
        print(ValueError)


def p1win_game(p1_score, p2_score):
    p1_score += 1
    p1_win = input("P1 wins! Try again? y/n ").lower()
    if p1_win == "y":
        return rock_paper_scissors(p1_score, p2_score)
    elif p1_win == "n":
        print("Good Game!")
        scoring(p1_score, p2_score)
    else:
        return ValueError


def p2win_game(p1_score, p2_score):
    p2_score += 1
    p2_win = input("P2 wins! Try again? y/n ").lower()
    if p2_win == "y":
        return rock_paper_scissors(p1_score, p2_score)
    elif p2_win == "n":
        print("Good Game!")
        scoring(p1_score, p2_score)
    else:
        return ValueError


def scoring(p1_score, p2_score):
    print("P1: " + str(p1_score))
    print("P2: " + str(p2_score))
    if p1_score == p2_score:
        print("DRAW")
    elif p1_score > p2_score:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")


rock_paper_scissors(0, 0)
