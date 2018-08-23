import copy

N_ROWS = 7
N_COLS = 6

def printBoard(board):
	for i in range(0,6):
		for j in range(0, 7):
			print(board[j][5-i], end="")
		print(" ")

def createBoard():
	board = []
	for i in range(0, N_ROWS):
		row = []
		for j in range(0, N_COLS):
			row.append('_')
			# row.append(str(i*N_ROWS+j) + '  ')
		board.append(row)
	return board

def nextPlayer(player):
	if player == 'X':
		return 'O'
	else:
		return 'X'

def buildSegs(board):
	segs = []
	seg = []
	for i in range(0, 4):
		for j in range(0, 6):
			seg.append(board[i][j])
			seg.append(board[i+1][j])
			seg.append(board[i+2][j])
			seg.append(board[i+3][j])
			segs.append(seg)
			seg = []
	for i in range(0, 7):
		for j in  range(0, 3):
			seg.append(board[i][j])
			seg.append(board[i][j+1])
			seg.append(board[i][j+2])
			seg.append(board[i][j+3])
			segs.append(seg)
			seg = []
	for i in range(0, 3):
		for j in range(i, 3):
			seg.append(board[i][j])
			seg.append(board[i+1][j+1])
			seg.append(board[i+2][j+2])
			seg.append(board[i+3][j+3])
			segs.append(seg)
			seg = []
	for row in board:
		row.reverse()
	for i in range(0, 3):
		for j in range(i, 3):
			seg.append(board[i][j])
			seg.append(board[i+1][j+1])
			seg.append(board[i+2][j+2])
			seg.append(board[i+3][j+3])
			segs.append(seg)
			seg = []
	board.reverse()
	for i in range(0, 3):
		for j in range(i, 3):
			seg.append(board[i][j])
			seg.append(board[i+1][j+1])
			seg.append(board[i+2][j+2])
			seg.append(board[i+3][j+3])
			segs.append(seg)
			seg = []
	for row in board:
		row.reverse();
	for i in range(0, 3):
		for j in range(i, 3):
			seg.append(board[i][j])
			seg.append(board[i+1][j+1])
			seg.append(board[i+2][j+2])
			seg.append(board[i+3][j+3])
			segs.append(seg)
			seg = []
	board.reverse()
	return segs

def segValue(seg):
	x = seg.count('X')
	o = seg.count('O')
	if x == 4:
		return 1024
	elif o == 4:
		return -1024
	elif x == 3 and o == 0:
		return 50
	elif x == 0 and o == 3:
		return -50
	elif x == 2 and o == 0:
		return 10
	elif x == 0 and o == 2:
		return -10
	elif x == 1 and o == 0:
		return 1
	elif x == 0 and o == 1:
		return -1
	else:
		return 0

def boardValue(player, board):
	segs = buildSegs(board)
	value = 0
	for seg in segs:
		value += segValue(seg)
	if player == 'X':
		return 16 + value
	else:
		return -16 + value

def validMoves(board):
	moves = []
	i = 0
	for col in board:
		if col.count('_') > 0:
			moves.append(i)
		i += 1
	return moves

def makeMove(player, move, board):
	new_board = []
	for i in board:
		row = []
		for j in i:
			row.append(j)
		new_board.append(row)
	i = new_board[move].index('_')
	new_board[move][i] = player
	return new_board

def maior(x, y):
	return x > y

def menor(x, y):
	return x < y

def test_minimax(player):
	if player == 'X':
		return maior
	else:
		return menor

def minimax(player, board, test, depth):
	value = boardValue(player, board)
	if depth <= 0 or value > 512 or value < -512:
		return 0, value
	temp_player = nextPlayer(player)
	moves = validMoves(board)
	best_val = float('inf') if test(float('-inf'), float('inf')) else float('-inf')
	best_move = 0
	for mov in moves:
		temp_board = makeMove(player, mov, board)
		# val = boardValue(temp_player, temp_board)
		lixo, val = minimax(temp_player, temp_board, test_minimax(temp_player), depth - 1)
		if test(val, best_val):
			best_move, best_val = mov, val
		# print(mov, val)
	return best_move, best_val

def alfabeta(player, board, test, depth, alfa, beta):
	value = boardValue(player, board)
	if depth <= 0 or value > 512 or value < -512:
		return 0, value
	temp_player = nextPlayer(player)
	moves = validMoves(board)
	best_val = float('inf') if test(float('-inf'), float('inf')) else float('-inf')
	best_move = 0
	for mov in moves:
		temp_board = makeMove(player, mov, board)
		# val = boardValue(temp_player, temp_board)
		lixo, val = alfabeta(temp_player, temp_board, test_minimax(temp_player), depth - 1, alfa, beta)
		if test(val, best_val):
			best_move, best_val = mov, val
		if test == maior:
			alfa = max(alfa, best_val)
		elif test == menor:
			beta = min(beta, best_val)
		if beta <= alfa:
			break
		# print(mov, val)
	return best_move, best_val

board = createBoard()
# printBoard(board)

player = 'X'
# print(boardValue(player, board))
fim = False

alg = input("Escolha o algoritmo:\n1-Minimax\n2-Alfa-beta\n")
while not fim:
	printBoard(board)
	val = boardValue(player, board)
	print(val)
	if val > 512:
		print('X ganhou!')
		fim = True
	elif val < -512:
		print('O ganhou!')
		fim = True
	val_moves = validMoves(board)
	depth = 13 - len(val_moves)
	# print(depth)
	# print(val_moves)
	player_string = "Player " + player + ' move: '
	valid_move = False
	while not valid_move:
		if player == 'X':
			move = input(player_string)
			# move, lixo = minimax(player, board, test_minimax(player), depth)
			# print(player_string + str(move))
		else:
			if alg == 1:
				move, lixo = minimax(player, board, test_minimax(player), depth)
			else:
				move, lixo = alfabeta(player, board, test_minimax(player), depth, float('-inf'), float('inf'))	
			# move = input(player_string)
			# move, lixo = minimax(player, board, test_minimax(player), 5)
			# print(player_string + str(move))
			# move, lixo = alfabeta(board, player, depth, , True)
			print(player_string + str(move))
		try:
			move_index = int(move)
			i = board[move_index].index('_')
			board[move_index][i] = player
			player = nextPlayer(player)
			valid_move = True
		except:
			print("Invalid move!")
			break
		# for row in buildSegs(board):