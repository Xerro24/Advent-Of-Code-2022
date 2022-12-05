print('\n\n\n')


score = 0
with open('Strategy Guide.txt', 'r') as file:
    for line in file:
        Opponent_move = line.split(" ")[0]
        Player_move = line.split(" ")[1]
        Player_move = Player_move.split("\n")[0]
        print(Opponent_move,Player_move)
        score += ord(Player_move)-87
        Player_move = ord(Player_move)-87
        Opponent_move = ord(Opponent_move)-64
        #print(Opponent_move,Player_move)
        if (Player_move - 1 == Opponent_move or Player_move + 2 == Opponent_move):
            score += 6
        elif (Player_move == Opponent_move):
            score += 3
        print(score)




print('\n\n\n')