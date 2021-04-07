board = ['-','-','-',
        '-','-', '-',
        '-','-','-']

game_ongoing = True
player = ['X', 'O']
current_player = player[0]


def display_board():
    print('         ' + board[0] + '|' + board[1] + '|' + board[2])
    print('         ' + board[3] + '|' + board[4] + '|' + board[5])
    print('         ' + board[6] + '|' + board[7] + '|' + board[8])
    print(' ')


def display_header():
    print('********** Player 1 -------> X ***********')
    print('********** Player 2 -------> O ***********')


def get_current_player():
    return current_player


def flip_player():
    current = get_current_player()
    next_player = player[1] if current == 'X' else player[0]
    return next_player


def get_player_entry(player):
    present = player
    present_player = 'Player 1' if player == 'X' else 'Player 2'
    try:
        entry = input('{}. Enter a number between 1-9: '.format(present_player))
        position = int(entry)
        if(position >= 1 and position <= 9):
            if board[position - 1] != '-':
                print('Space not available!')
                get_player_entry(present)
            else:
                board[position - 1] = player
                display_board()
        else:
            print('Entries are valid between 1-9!!!')
            get_player_entry(present)
    except Exception:
        print('Entries are valid between 1-9!!!')
        get_player_entry(present)


def check_win():
    if check_column():
        declare_winner(check_column())
        return True
    if check_row():
        declare_winner(check_row())
        return True
    if check_diagonal():
        declare_winner(check_diagonal())
        return True


def check_row():
    if board[0] == board[1] and board[0] == board[2]:
        if board[0] != '-':
            return check_winner(board[0])   
    if board[3] == board[4] and board[3] == board[5]:
        if board[3] != '-':
            return check_winner(board[3])
    if board[6] == board[7] and board[6] == board[8]:
        if board[6] != '-':
            return check_winner(board[6])


def check_column():
    if board[0] == board[3] and board[0] == board[6]:
        if board[0] != '-':
            return check_winner(board[0])   
    if board[1] == board[4] and board[1] == board[7]:
        if board[1] != '-':
            return check_winner(board[3])
    if board[2] == board[5] and board[2] == board[8]:
        if board[2] != '-':
            return check_winner(board[2])


def check_diagonal():
    if board[0] == board[4] and board[0] == board[8]:
        if board[0] != '-':
            return check_winner(board[0])   
    if board[2] == board[4] and board[2] == board[6]:
        if board[2] != '-':
            return check_winner(board[3])
    

def check_winner(position):
    if position == 'X':
        return 'Player 1'
    return 'Player 2'


def declare_winner(winner):
    print('{} is the winner!'.format(winner))       


def reset_board():
    for x in range(9):
        board[x] = '-'


def ask_for_replay():
    answer = input('Will you play again? (y/n): ')
    if answer == 'y' or answer == 'Y':
        reset_board()
        play_game()

def check_tie():
    full_occupied = None
    for x in range(9):
        if board[x] == '-':
            full_occupied = False
            break
        else:
            full_occupied = True
    if full_occupied:
        print('It\'s a tie')
        ask_for_replay()
        return True

def play_game():
    display_header()
    display_board()
    while game_ongoing:
        get_player_entry(get_current_player())
        if check_win():
            ask_for_replay()
            break
        else:
            if check_tie():
                break
        get_player_entry(flip_player())
        if check_win():
            ask_for_replay()
            break
        else:
            if check_tie():
                break


play_game()