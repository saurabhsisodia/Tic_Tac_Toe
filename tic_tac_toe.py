def print_board(board):
    print(board['top-l']+'|',board['top-m']+'|',board['top-r']+'|')
    print('--------')
    print(board['mid-l']+'|',board['mid-m']+'|',board['mid-r']+'|')
    print('--------')
    print(board['low-l']+'|',board['low-m']+'|',board['low-r']+'|')
    print('--------')

def Winner(board):
    if board['top-l']==board['top-m']==board['top-r']!=' ':
        return True
    elif board['mid-l']==board['mid-m']==board['mid-r']!=' ':
        return True
    elif board['low-l']==board['low-m']==board['low-r']!=' ':
        return True
    elif board['top-l']==board['mid-l']==board['low-l']!=' ':
        return True
    elif board['top-m']==board['mid-m']==board['low-m']!=' ':
        return True
    elif board['top-r']==board['mid-r']==board['low-r']!=' ':
        return True
    elif board['top-l']==board['mid-m']==board['low-r']!=' ':
        return True
    elif board['low-l']==board['mid-m']==board['top-r']!=' ':
        return True
    else:
        return False

board={"top-l":' ',"top-m":' ',"top-r":' ',
             "mid-l":' ',"mid-m":' ',"mid-r":' ',
             "low-l":' ',"low-m":' ',"low-r":' '}
turn='X'
for i in range(9):
    print_board(board)
    print("turn for",turn,"move on which space")
    move=input()
    if board[move]!=' ':
        print("wrong place please start game again")
        break
    board[move]=turn
    win=Winner(board)
    if win:
        print(turn,"win this game")
        break
    if turn =='X':
        turn ='0'
    else:
        turn ='X'
print_board(board)

