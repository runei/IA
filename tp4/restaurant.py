import csv

class Node:
	def __init__(self, name):
		self.name = name
		self.childs = []

	def addChild(self, node):
		self.childs.append(node)

costumers = csv.DictReader(open('restaurant.csv'))

for row in costumers:
	for key, val in row.items():
		

def entropy(vector, target):
	total = 0.0
	for i in range(0, )
