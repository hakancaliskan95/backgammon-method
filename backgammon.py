def find_moves(checkers, dice1, dice2):
     #controling input
    if dice1<1 or dice1>6 or dice2<1 or dice2>6:
        return "Please try again"
    
    ##important doors have defined
    important_doors = [5, 6, 7, 8, 17, 18, 19, 20]
    filled = []
    result = []

print(find_moves(checkers,dice1,dice2))