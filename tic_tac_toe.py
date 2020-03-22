print("Welcome to Tic Tac Toe Game!")
print()
print('Grab your friend!')
print("And let's play!\n")
player1 = '>Player1<'
player2 = '>Player2<'

# Enter players' names 
def enter_name():
    global player1, player2 
    player1 = '>Player1<'
    player2 = '>Player2<'
    print(f'{player1} Enter your name, please:')
    player1=input()
    player1='>{}<'.format(player1)
    print(f'Welcome {player1}!')
    print(f'\n{player2} Enter your name, please:')
    player2=input()
    player2='>{}<'.format(player2)
    print(f'Welcome {player2}!')

# Choosing X or O
def XorO():
    global player1, player2
    print(f'\n{player1} Do you want to be X or O?')
    cond = True
    while cond:
        inp1 = input("")
        if inp1.upper() == 'X':
            global turn
            print(f'{player1} starts the game!')
            cond = False
        elif inp1.upper() == 'O':
            print(f'{player2} starts the game!')
            cond = False
            temp = player1
            player1 = player2
            player2 = temp 
        else:
            print('Please choose X or O!')

#Shows rules for making a move 
def board_example():
    print('Numbers represent the position of X or O and reflect NumPad on keyboard')
    board_example = '{0:^3} | {1:^3} | {2:^3}\n{3:^3} | {4:^3} | {5:^3}\n{6:^3} | {7:^3} | {8:^3}\n'.format(7,8,9,4,5,6,1,2,3)
    print(board_example)

# Making a move 
def choose_num():
    global turn
    if turn % 2 == 0: 
        num = input(f'{player2}, please choose field from 1 to 9\n')
    else:
        num = input(f'{player1}, please choose field from 1 to 9\n')
    if num.isdigit() and int(num)<=9 and int(num)>=1: # Check if input is correct
        
        # Check if field is empty
        
        def checker():
            if d[f'{int(num)}'] == 'O' or d[f'{int(num)}'] == 'X':
                print(f'The field {num} is already taken!')
                choose_num()
            else:
                if turn % 2 == 0:
                    d[f'{int(num)}'] = 'O'
                else:
                    d[f'{int(num)}'] = 'X'
        checker()   
    else:
        print('Incorrect input!')
        choose_num()
    
def board():
    board = '{x7:^3} | {x8:^3} | {x9:^3}\n{x4:^3} | {x5:^3} | {x6:^3}\n{x1:^3} | {x2:^3} | {x3:^3}\n'.format(x7=d['7'],x8=d['8'],x9=d['9'],x4=d['4'],x5=d['5'],x6=d['6'],x1=d['1'],x2=d['2'],x3=d['3'])
    
    print(board)
# Winning conditions
def win():    
    if d['1'] == d['2'] == d['3'] !='-' or \
    d['4'] == d['5'] == d['6'] != '-' or \
    d['7'] == d['8'] == d['9'] != '-' or \
    d['1'] == d['4'] == d['7'] != '-' or \
    d['2'] == d['5'] == d['8'] != '-' or \
    d['3'] == d['6'] == d['9'] != '-' or \
    d['1'] == d['5'] == d['9'] != '-' or \
    d['7'] == d['5'] == d['3'] != '-':
        global cond 
        cond = False
        if turn % 2 == 0:
            print(f'{player2} wins!')
        else:
            print(f'{player1} wins!') 
    return
def game():
	global turn, d, cond 
	XorO()
	board_example()
	d = {'1':'-','2':'-','3':'-','4':'-','5':'-','6':'-','7':'-','8':'-','9':'-'}
	turn = 1
	cond = True
	while cond and turn <=9:
		choose_num()
		board()
		win()
		turn += 1
		if turn == 9:
			print("It's a tie!")
	replay()
def replay():
	replay = input('Wanna play again? Y or N\n')
	if replay.upper() == 'Y':
		cond = True
		while cond:
			name_change = input('Change names? Y or N\n')
			if name_change.upper()=='Y':
				enter_name()
				game()
				cond = False
			elif name_change.upper()=='N':
				game()
				cond = False
			else:
				print('Incorrect input!')
	elif replay.upper() == 'N':
		quit()
	else:
		print('Incorrect input!')
		replay()

enter_name()
game()