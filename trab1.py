import time

N_COLS = 4
N_ROWS = 4

def moveLeft(pos, node):
	result = list(node)
	result[pos], result[pos - 1] = result[pos - 1], result[pos]
	return result

def moveRight(pos, node):
	result = list(node)
	result[pos], result[pos + 1] = result[pos + 1], result[pos]
	return result

def moveUp(pos, node):
	result = list(node)
	result[pos], result[pos - N_COLS] = result[pos - N_COLS], result[pos]
	return result

def moveDown(pos, node):
	result = list(node)
	result[pos], result[pos + N_COLS] = result[pos + N_COLS], result[pos]
	return result

def makeDescendants(node):
	descendant_list = []
	zero_pos = node.index(0)
	if zero_pos % N_COLS != 0:
		descendant_list.append(moveLeft(zero_pos, node))
	if (zero_pos + 1) % N_COLS != 0:
		descendant_list.append(moveRight(zero_pos, node))
	if zero_pos >= N_COLS:
		descendant_list.append(moveUp(zero_pos, node))
	if zero_pos < len(node) - N_COLS:
		descendant_list.append(moveDown(zero_pos, node))
	return descendant_list

def removeFrontNodeFrom(queue):
	pass

def insert(descendants, queue, explored, solution, queueing_function):
	return queueing_function(descendants, queue, explored, solution)

def bfs(descendants, queue, explored, solution):
	still_valid_path = False
	for node in descendants:
		if node not in explored:
			queue.append(node)
			still_valid_path = True
	if not still_valid_path:
		# print("Caminho errado!")
		return False
	return True

def dfs(descendants, queue, explored, solution):
	still_valid_path = False
	for node in reversed(descendants):
		if node not in explored:
			queue.insert(0, node)
			still_valid_path = True
	if not still_valid_path:
		print("Caminho errado!")
		return False
	return True	

def distance(v1, v2):
	dist = 0
	for i, val in enumerate(v2):
		if val != 0:
			v2i = i // 4
			v2j = i % 4
			indexv1 = v1.index(val)
			v1i = indexv1 // 4
			v1j = indexv1 % 4
			dist += abs(v2i - v1i) + abs(v2j - v1j)
	return dist

def greedy(descendants, queue, explored, solution):
	dist_desc = []
	still_valid_path = False
	for node in descendants:
		if node not in explored:
			still_valid_path = True
			dist = distance(node, solution)
			if dist_desc == []:
				queue.insert(0, node)
				dist_desc.append(dist)
			else:
				for i, dd in enumerate(dist_desc):
					if dd > dist:
						dist_desc.insert(i, dist)
						queue.insert(i, node)
						break
				else:
					dist_desc.append(dist)
					queue.insert(len(dist_desc), node)
	if not still_valid_path:
		print("Caminho errado!")
	# q = ordered_descendants + queue
	# queue = q

def generalSearchAlgorithm(ini, solution, queueing_function):
	explored = []
	unexplored = []
	unexplored.append(ini)
	while unexplored != []:
		node = unexplored.pop(0)
		# print(len(unexplored))
		if node == solution:
			unexplored = []
		else:
			explored.append(node)
			# printBoard(node)
			# print(node)
			descendants = makeDescendants(node)
			insert(descendants, unexplored, explored, solution, queueing_function)		
			# print(unexplored)
	print(solution)

def printBoard(node):
	print("---------------------------------")
	for i in range(0, N_COLS):
		for j in range(0, N_ROWS):
			print("| %2d | " % node[i*4+j], end="")
		print("")
	print("---------------------------------")

ini = [1,2,3,4,5,6,8,12,13,9,0,7,14,11,10,15]
# ini = [1,2,3,4,13,6,8,12,5,9,0,7,14,11,10,15]
solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
# printBoard(ini)

start_time = time.time()
generalSearchAlgorithm(ini, solution, dfs)
elapsed_time = time.time() - start_time

print("Time: %ds" % elapsed_time)