def find_moves(checkers, dice1, dice2):
     #controling input
    if dice1<1 or dice1>6 or dice2<1 or dice2>6:
        return "Please try again"

print(find_moves(checkers,dice1,dice2))