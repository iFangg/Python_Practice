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


def play_again(msg, p1_score, p2_score):
    answer = input(msg + " Try again? y/n ").lower()
    if answer == "y":
        return rock_paper_scissors(p1_score, p2_score)
    elif answer == "n":
        print("Good Game(s)!")
        scoring(p1_score, p2_score)
    else:
        print("ERROR")
        return play_again(msg, p1_score, p2_score)


def draw_game(p1_score, p2_score):
    play_again("DRAW!", p1_score, p2_score)


def win_game(msg, p1_score, p2_score):
    if msg == "P1":
        p1_score += 1
    else:
        p2_score += 1
    play_again(msg + " wins!", p1_score, p2_score)


def scoring(p1_score, p2_score):
    print("P1: " + str(p1_score) + "\nP2: " + str(p2_score))
    if p1_score == p2_score:
        print("DRAW!")
    elif p1_score > p2_score:
        print("Player 1 Wins!")
    else:
        print("Player 2 Wins!")


if __name__ == "__main__":
    rock_paper_scissors(0, 0)
