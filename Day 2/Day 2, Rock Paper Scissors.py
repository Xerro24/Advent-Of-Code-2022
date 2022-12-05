print('\n\n\n')


score = 0
with open('Strategy Guide.txt', 'r') as file:
    for line in file:
        Opponent_move = line.split(" ")[0]
        End_State = line.split(" ")[1]
        End_State = End_State.split("\n")[0]
        print(Opponent_move,End_State)
        
        End_State = ord(End_State)-87
        Opponent_move = ord(Opponent_move)-64
        if End_State == 2:
            score += 3
        elif End_State == 3:
            score += 6
        

        #print(Opponent_move,Player_move)
        if (End_State == 1):
            if (Opponent_move != 1):
                score += Opponent_move-1
            else:
                score += 3
        elif (End_State == 2):
            score += Opponent_move
        else:
            if (Opponent_move != 3):
                score += Opponent_move+1
            else:
                score += 1
        print(score)




print('\n\n\n')