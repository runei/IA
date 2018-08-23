import time

N_COLS = 4
N_ROWS = 4
NO_LIMIT = -1

class Node:
	def __init__(self, node, depth):
		self.node = node
		self.depth = depth

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

def makeDescendants(node, explored, limit):
	result = []
	new_depth = node.depth + 1
	if limit != NO_LIMIT and new_depth > limit:
		return result
	descendant_list = []
	zero_pos = node.node.index(0)
	if zero_pos % N_COLS != 0:
		descendant_list.append(moveLeft(zero_pos, node.node))
	if (zero_pos + 1) % N_COLS != 0:
		descendant_list.append(moveRight(zero_pos, node.node))
	if zero_pos >= N_COLS:
		descendant_list.append(moveUp(zero_pos, node.node))
	if zero_pos < len(node.node) - N_COLS:
		descendant_list.append(moveDown(zero_pos, node.node))
	#delete the ones that already have been explored
	for des in descendant_list:
		if des not in explored:
			result.append(Node(des, new_depth))
	# descendant_list[:] = [des for des in descendant_list if des not in explored]
	return result

def generalSearch(ini, solution, insert_fn, limit):
	explored = []
	unexplored = []
	unexplored.append(Node(ini, 0))
	count = 0
	while unexplored != []:
		node = unexplored.pop(0)
		count += 1
		# print(node)
		if node.node == solution:
			print("Nodes: %d" % count)
			return node
		explored.append(node)
		descendants = makeDescendants(node, explored, limit)
		insert_fn(unexplored, descendants)
	return False

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

def enqueueAtEnd(queue, descendants):
	queue.extend(descendants)

def enqueueAtBegin(queue, descendants):
	#dont do this
	for d in reversed(descendants):
		queue.insert(0, d)

def enqueueGreedy(queue, descendants):
	dist_desc = []
	for node in descendants:
		dist = distance(node.node, solution)
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

def bfs(ini, solution):
	return generalSearch(ini, solution, enqueueAtEnd, NO_LIMIT)

def dfs(ini, solution):
	return generalSearch(ini, solution, enqueueAtBegin, NO_LIMIT)

def idfs(ini, solution):
	depth = 0
	while True:
		result = generalSearch(ini, solution, enqueueAtBegin, depth)
		if result:
			return result
		depth += 1

def greedy(ini, solution):
	return generalSearch(ini, solution, enqueueGreedy, NO_LIMIT)

def inversionCount(ini, solution):
	inv_count = 0
	for i in range(0, len(ini) - 1):
		for j in range(i + 1, len(solution)):
			if i > solution.index(j):
				inv_count += 1
	return inv_count

def isSolvable(ini):
	pass

def readBoard(string):
	res = []
	print(string)
	i = 0
	while i < N_ROWS:
		inp = list(map(int, input().split()))
		if len(inp) != 4:
			print("Digite 4 colunas")
		else:
			res.extend(inp)
			i += 1
	return res

ini = [1,8,2,0,4,3,7,6,5]
# ini = [13,2,10,3,1,12,8,4,5,0,9,6,15,14,11,7]
solution = [1,2,3,4,5,6,7,8,0]

print(inversionCount(ini, solution))
quit()

ini = readBoard("Digite a configuracao inicial:")
solution = readBoard("Digite a solucao:")
while True:
	inp = int(input("Escolha o metodo de busca\n1 - BFS\n2 - DFS\n3 - IDFS\n4 - Gulosa\n"))
	if inp > 4 or inp < 1:	
		print("Comando Invalido")
	else:
		break

start_time = time.time()
if inp == 1:
	result = bfs(ini, solution)
elif inp == 2:
	result = dfs(ini, solution)
elif inp == 3:
	result = idfs(ini, solution)
elif inp == 4:
	result = greedy(ini, solution)
elapsed_time = time.time() - start_time

print("Time: %ds\nDepth: %d" % (elapsed_time, result.depth))

# print(ini)
"""solution = []
print("Digite a configuracao inicial:\n")
for i in range(0, N_ROWS):


ini = [1,2,3,4,5,0,7,8,9,6,10,12,13,14,11,15]
# ini = [1,2,3,4,13,6,8,12,5,9,0,7,14,11,10,15]
solution = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]

start_time = time.time()
result = dfs(ini, solution)
elapsed_time = time.time() - start_time

print("Time: %ds\nDepth: %d" % (elapsed_time, result.depth))"""