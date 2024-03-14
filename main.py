#Jayda Fountain
player = "A"
again = False
player_count = 2
win = False
# create your board variable
#        0  1  2  3  4  5  6  7  8  9  10 11 12 13
board = [0, 4, 4, 4, 4, 4, 4, 0, 4, 4, 4, 4, 4, 4]
# create your print_board function
def print_board():
    print("         13     12     11     10     9     8")
    print("--------------------------------------------------")
    print("B:       " + str(board[13]) + "      "+str(board[12])+\
        "      "+str(board[11])+"      "+str(board[10])+"      "+\
        str(board[9])+"     "+str(board[8]))
    print("    "+str(board[0])+"                               "+\
        "            "+str(board[7]))
    print("A:       " + str(board[1]) + "      "+str(board[2])+\
        "      "+str(board[3])+"      "+str(board[4])+"      "+\
        str(board[5])+"     "+str(board[6]))
    print("--------------------------------------------------")
    print("         1      2      3      4      5     6")
    
    if(win == False):
        take_turn()
    
#            P1    P2     P3     P4      P5     P6
A_valid = [False, False, False, False, False, False]
#            P8     P9    P10    P11    P12    P13
B_valid = [False, False, False, False, False, False]


def is_valid_move():
    global valid_moves
    valid = False
    valid_moves = []
    if(player == "A"):
        for num in range(1, 7):
            if(board[num] > 0):
                valid = True
                A_valid[num - 1] = valid
        
        for value in range(len(A_valid)):
            if(A_valid[value] == True):
                valid_moves.append(str(value + 1))
        
        print("Possible moves: " + ', '.join(valid_moves))
        
    elif(player == "B"):
        for num in range(8, 14):
            if(board[num] > 0):
                valid = True
                B_valid[num - 8] = valid
        
        for value in range(len(B_valid)):
            if(B_valid[value] == True):
                valid_moves.append(str(value + 8))
        
        print("Possible moves: " + ', '.join(valid_moves))
    
    
def move_stones(pocket_num):
    #variables
    global player, again, player_count
    pocket_num = int(pocket_num)
    other_pockets = board[pocket_num] + 1
    A_score = board[7]
    B_score = board[0]
    pocket8 = board[8]
    pocket1 = board[1]
    pair1 = [1, 13]
    pair2 = [2, 12]
    pair3 = [3, 11]
    pair4 = [4, 10]
    pair5 = [5, 9]
    pair6 = [6, 8]
    all_pairs = [pair1, pair2, pair3, pair4, pair5, pair6]
    p1 = False
    p2 = False
    p3 = False
    p4 = False
    p5 = False
    p6 = False
    
    if(board[pocket_num] + pocket_num in pair1 \
        or board[pocket_num] + pocket_num - 14 in pair1):
        p1 = True
    elif(board[pocket_num] + pocket_num in pair2 \
        or board[pocket_num] + pocket_num - 14 in pair2):
        p2 = True
    elif(board[pocket_num] + pocket_num in pair3 \
        or board[pocket_num] + pocket_num - 14 in pair3):
        p3 = True
    elif(board[pocket_num] + pocket_num in pair4 \
        or board[pocket_num] + pocket_num - 14 in pair4):
        p4 = True
    elif(board[pocket_num] + pocket_num in pair5 \
        or board[pocket_num] + pocket_num - 14 in pair5):
        p5 = True
    elif(board[pocket_num] + pocket_num in pair6 \
        or board[pocket_num] + pocket_num - 14 in pair6):
        p6 = True
    
    
    all_p_nums = [p1, p2, p3, p4, p5, p6]
    
    
    
    if(player == "A"):
        try:
            number = board[board[pocket_num] + pocket_num]
        except IndexError:
            number = board[board[pocket_num] + pocket_num - 14]
        
        count = board[pocket_num]
        
        if(board[pocket_num] + pocket_num > 13):
            board[0] -= 1
            for stone in range(board[pocket_num] + 2):
                try:
                    board[pocket_num + stone] += 1
                except IndexError:
                    step1 = (pocket_num + stone) - 14
                    board[step1] += 1
                count -= 1
                if(count == -1 and board[7] == (A_score + 1) and board[8] == pocket8):
                    player = "A"
                    again = True
                    
                for boolean in range(len(all_p_nums)):
                    if(count == -1 and number == 0 and all_p_nums[boolean] == True):
                        new = all_pairs[boolean]
                        
                        if(board[pocket_num] + pocket_num > 7 and pocket_num in new):
                            #board[7] += board[new[1]]
                            pass
                        
                        elif(board[pocket_num] + pocket_num > 7):
                            #board[7] += board[new[0]]
                            pass
                        
                        elif(board[new[1]] != 0):
                            board[7] += board[new[1]] + 1
                            board[new[0]] = 0
                            board[new[1]] = 0
        else:
            for stone in range(board[pocket_num] + 1):
                try:
                    board[pocket_num + stone] += 1
                except IndexError:
                    step1 = (pocket_num + stone) - 14
                    board[step1] += 1
                count -= 1
                if(count == -1 and board[7] == (A_score + 1) and board[8] == pocket8):
                    player = "A"
                    again = True
                    
                for boolean in range(len(all_p_nums)):
                    if(count == -1 and number == 0 and all_p_nums[boolean] == True):
                        new = all_pairs[boolean]
                        
                        if(board[pocket_num] + pocket_num > 7 and pocket_num in new):
                            #board[7] += board[new[1]]
                            pass
                        
                        elif(board[pocket_num] + pocket_num > 7):
                            #board[7] += board[new[0]]
                            pass
                        
                        elif(board[new[1]] != 0):
                            board[7] += board[new[1]] + 1
                            board[new[0]] = 0
                            board[new[1]] = 0
    
        
    if(player == "B"):
        number = board[board[pocket_num] + pocket_num - 14]
        count = board[pocket_num]
        
        if(board[pocket_num] + pocket_num - 14 > 6):
            board[7] -= 1
            for stone in range(board[pocket_num] + 2):
                try:
                    board[pocket_num + stone] += 1
                except IndexError:
                    step1 = (pocket_num + stone) - 14
                    board[step1] += 1
                count -= 1
                if(count == -1 and board[0] == (B_score + 1) and board[1] == pocket1):
                    player = "B"
                    again = True
                
                for boolean in range(len(all_p_nums)):
                    if(count == -1 and number == 0 and all_p_nums[boolean] == True):
                        new = all_pairs[boolean]
                        
                        if(board[pocket_num] + pocket_num > 13 and pocket_num in new):
                            #board[0] += board[new[0]]
                            pass
                        
                        elif(board[pocket_num] + pocket_num > 13):
                            #board[0] += board[new[1]]
                            pass
                        
                        elif(board[new[0]] != 0):
                            board[0] += board[new[0]] + 1
                            board[new[0]] = 0
                            board[new[1]] = 0

        else:
            for stone in range(board[pocket_num] + 1):
                try:
                    board[pocket_num + stone] += 1
                except IndexError:
                    step1 = (pocket_num + stone) - 14
                    board[step1] += 1
                count -= 1
                if(count == -1 and board[0] == (B_score + 1) and board[1] == pocket1):
                    player = "B"
                    again = True
                
                for boolean in range(len(all_p_nums)):
                    if(count == -1 and number == 0 and all_p_nums[boolean] == True):
                        new = all_pairs[boolean]
                        
                        if(board[pocket_num] + pocket_num - 14 > 13 and pocket_num in new):
                            #board[0] += board[new[0]]
                            pass
                        
                        elif(board[pocket_num] + pocket_num - 14 > 13):
                            #board[0] += board[new[1]]
                            pass
                        
                        elif(board[new[0]] != 0):
                            board[0] += board[new[0]] + 1
                            board[new[0]] = 0
                            board[new[1]] = 0
                    
    board[pocket_num] = 0
    
    
    
    
def take_turn():
    global again, player, player_count, valid_moves
    
    if(again == True):
        print("Go Again!")
    else:
        if(player_count % 2 == 0):
            player = "A"
        else:
            player = "B"
    
    print("Player " + player + "'s Turn!")
    is_valid_move()
    pocket_num = input("Choose a pocket: ")
    while pocket_num not in valid_moves:
        pocket_num = input("Not a possible move! Choose a pocket: ")
    
    again = False
    move_stones(pocket_num)
    
    
def calculate_winner():
    if(board[0] > board[7]):
        print("Player B wins!")
        print("Score: " + str(board[0]) + " - " + str(board[7]))
        #break
    elif(board[7] > board[0]):
        print("Player A wins!")
        print("Score: " + str(board[0]) + " - " + str(board[7]))
        #break
    
def game_over():
    global win
    if(board[1] == 0 and board[2] == 0 and board[3] == 0 and board[4] == 0 \
        and board[5] == 0 and board[6] == 0):
        win = True
        board[0] += board[8] + board[9] + board[10] + board[11] + board[12] + board[13]
        for num in range(8, 14):
            board[num] = 0
        print_board()
        calculate_winner()
    
    elif(board[8] == 0 and board[9] == 0 and board[10] == 0 and board[11] == 0 \
        and board[12] == 0 and board[13] == 0):
        win = True
        board[7] += board[1] + board[2] + board[3] + board[4] + board[5] + board[6]
        for num in range(1, 7):
            board[num] = 0
        print_board()
        calculate_winner()
    
    
while True:
    print_board()
    if(again == False):
        player_count += 1
    
    game_over()
    if(win == True):
        break