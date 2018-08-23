#include <iostream>
#include <vector>
#include <limits>

struct Node
{
	int h; //estimated cost of the cheapest path 
	int cost;
	std::vector<int> successors;

	Node(int _h, int _cost, std::vector<int> _successors) : h(_h), cost(_cost), successors(_successors) {};
};

int search(std::vector<Node> tree, Node node, int g, int bound)
{
	int f = g + node.h;
	if (f > bound) return f;
	std::cout << node.h << "\t";
	// if (node == 0) return 0;
	int min = std::numeric_limits<int>::max();
	for (int succ : node.successors)
	{
		int t = search(tree, tree[succ], g + tree[succ].cost, bound);
		min = std::min(t, min);
	}
	return min;
}

void ida_star(std::vector<Node> tree, Node root)
{
	int bound = root.h;
	while (1)
	{
		std::cout << "\n" << bound << "\n";
		int t = search(tree, root, 0, bound);
		// if (t == 0) return bound;
		if (t == std::numeric_limits<int>::max()) return;
		bound = t;
	}
}

void printTree(std::vector<Node> tree, Node node)
{
	std::cout << node.h << "\n";
	for (int succ : node.successors)
	{
		printTree(tree, tree[succ]);
	}
}

std::vector<Node> initializeTree()
{
	std::vector<Node> tree;

	tree.push_back(Node( 99, 0, { 1, 8 } ));
		tree.push_back(Node( 75, 25, { 2, 5 } ));
			tree.push_back(Node( 51, 25, { 3, 4 } ));
				tree.push_back(Node( 0, 75, { } ));
				tree.push_back(Node( 1, 69, { } ));
			tree.push_back(Node( 42, 35, { 6, 7 } ));
				tree.push_back(Node( 5, 45, { } ));
				tree.push_back(Node( 3, 48, { } ));
		tree.push_back(Node( 62, 40, { 9, 12 } ));
			tree.push_back(Node( 35, 30, { 10, 11 } ));
				tree.push_back(Node( 10, 30, { } ));
				tree.push_back(Node( 0, 41, { } ));
			tree.push_back(Node( 27, 40, { 13, 14 } ));
				tree.push_back(Node( 12, 21, { } ));
				tree.push_back(Node( 2, 32, { } ));

	return tree;
}

int main()
{
	std::vector<Node> tree = initializeTree();	

	// printTree(tree, tree[0]);

	ida_star(tree, tree[0]);

	return 0;
}