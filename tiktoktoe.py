board = [["1","2","3"],["4","5","6"],["7","8","9"]]
win_flag = False
cats_count = 0
def game_mechanics(board, player):
    if player == 1:
        symbol = 'X'
    elif player == 2:
        symbol = 'O'
    list_in_list = []
    new_list = []
    board = sum(board, [])
    while True:
        try:
            print(f"User {player}, please type number 1-9")
            user_input = int(input())
            if user_input >= 1 and user_input <= 9 and board[user_input - 1] not in ["X", "O"]:
                break
            else:
                print("Please enter valid integer")
        except ValueError:
            print("Please enter valid integer")
            continue
    board[user_input - 1] = symbol

    for x in range(0, len(board), 3):
        list_in_list = board[x:x + 3]
        new_list.append(list_in_list)
    board = new_list
    print()
    for row in board:
        print(' '.join(row))
        if row == board[-1]:
            print()
    return board
def check_win(board, win_flag):
    if win_flag == False:
        for i in range(len(board)):
            for z in range(len(board)):
                if board[i][0] == board[i][1] and board[i][2] == board[i][1]:
                    win_flag = True
                if board[0][z] == board[1][z] and board[2][z] == board[1][z]:
                    win_flag = True
        if board[0][0] == board[1][1] and board[2][2] == board[1][1]:
                        win_flag = True
        if board[0][2] == board[1][1] and board[2][0] == board[1][1]:
                        win_flag = True
        return win_flag
    else:
         win_flag = False
         return win_flag
print()
for row in board:
    print(' '.join(row))
while True:
    board = game_mechanics(board, 1)
    cats_count = cats_count + 1
    if cats_count == 10:
        print("cats game")
        break
    win_flag = check_win(board, win_flag)
    if win_flag == False:
         pass
    elif win_flag == True:
        print("Player 1, You win")
        break
    if cats_count == 9:
        print("cats game")
        break
    board = game_mechanics(board, 2)
    cats_count = cats_count + 1
    win_flag = check_win(board, win_flag)
    if win_flag == False:
         pass
    elif  win_flag == True:
        print("Player 2, You win")
        break
    if cats_count == 9:
        print("cats game")
        break
