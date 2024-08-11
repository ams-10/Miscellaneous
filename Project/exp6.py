from collections import defaultdict

class Graph:
 	def __init__(self):
 		self.graph = defaultdict(list)
 		def add_edge(self, u, v):
 		self.graph[u].append(v)

 	def dfs_util(self, node, visited):
 		visited.add(node)
 		print(node, end=" ")

 		for neighbor in self.graph[node]:
 			if neighbor not in visited:
 				self.dfs_util(neighbor, visited)

 	def dfs(self, start_node):
		visited = set()
		self.dfs_util(start_node, visited)
# Example usage
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

start_node = 2
print("Depth-First Search Traversal starting from node", start_node)
graph.dfs(start_node)
