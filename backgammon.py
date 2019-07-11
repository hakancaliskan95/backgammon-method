def find_moves(checkers, dice1, dice2):
     #controling input
    if dice1<1 or dice1>6 or dice2<1 or dice2>6:
        return "Please try again"
    
    ##important doors have defined
    important_doors = [5, 6, 7, 8, 17, 18, 19, 20]
    filled = []
    result = []

    #calculating current score
    cur_score=0
    for i in checkers.keys():
        if checkers[i]==1:
            cur_score-=1
        if checkers[i]==2:
            if i in important_doors:
                cur_score+=2
            else:
                cur_score+=1
        if checkers[i]>2:
            filled.append(i)
            
            
    #finding possible moves       
    for key1 in checkers.keys():
        position1 = key1+dice1
        if position1>24:
            break
        for key2 in checkers.keys():
            position2 = key2+dice2
            if position2>24:
                break
            newCheckers = checkers.copy()
            if position1 in newCheckers:
                newCheckers[position1]+=1
            else:
                newCheckers[position1]=1
            newCheckers[key1]-=1
            if position2 in newCheckers:
                newCheckers[position2]+=1
            else:
                newCheckers[position2]=1
            newCheckers[key2]-=1
            
            #calculating final score
            score=0
            for i in newCheckers.keys():
                if newCheckers[i]==1:
                    score-=1
                if newCheckers[i]==2 and i not in filled:
                    if i in important_doors:
                        score+=2
                    else:
                        score+=1
            final_score = score-cur_score

            if final_score>0:
                result.append(((key1,position1),(key2,position2),final_score))
    return result
            
            
checkers = {1: 3, 6: 1, 10: 2, 12: 1, 13: 1}   
print(find_moves(checkers,2,1))