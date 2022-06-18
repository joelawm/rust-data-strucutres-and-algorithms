class Graph:
	adjacencyList = {}

	def __init__(self, nodes, edges):
		# Create all of the nodes
		for node in nodes:
			self.add_node(node)

		# Create all of the edges
		for edge_set in edges:
			self.add_edge(edge_set[0], edge_set[1])


	def add_node(self, node):
		self.adjacencyList.setdefault(node, set())

	# Add the edge
	# Undirected comment out the second add
	# Directed leave both
	def add_edge(self, node, edge):
		# Update both nodes so the edge raltionsip is added
		self.adjacencyList[node].add(edge)
		self.adjacencyList[edge].add(node)

	# Breadth First Search
	# Easiest to do
	# You visit each child of the parent if you find it then your good to go, if not you visit those childrens children.
	# Time Complexity: O(V+E) - Space Complexity: O(V)
	def BFS(self, start):
		visited = {}
		queue = []

		visited.setdefault(start)
		queue.append(start)

		while queue:
			s = queue.pop(0) 
			print (s, end = " ") 

			for neighbour in self.adjacencyList[s]:
				if neighbour not in visited:
					visited.setdefault(neighbour)
					queue.append(neighbour)
				
	# Depth First Search
	# You choose a branch and keep going down until every point is visited.
	# Time Complexity: O(V+E) - Space Complexity: O(V)
	def DFS(self, start, visited=None):
		if visited is None:
			visited = set()

		visited.add(start)

		print(start, end = " ")

		for next in self.adjacencyList[start] - visited:
			self.DFS(next, visited)
		return visited

def main():
	#nodes = "PHX BKK OKC JFK LAX MEX EZE HEL LOS LAP LIM".split(' ')
	#edges = [['PHX', 'LAX'],['PHX','JFK'],['JFK','OKC'],['JFK', 'HEL'],['JFK','LOS'],['MEX','LAX'],['MEX','BKK'],['MEX','LIM'],['MEX', 'EZE'],['LIM', 'BKK']]
	nodes = "a b c d e".split()
	edges = [["a","b"],["a","c"],["b","a"],["b","d"],["c","a"],["c","d"],["d","e"],["e","a"]]

	graph = Graph(nodes, edges)

	print("BFS ")
	graph.BFS('a')
	print("\nDFS ")
	graph.DFS('a')

if __name__ == "__main__":
    main()