import collections, math
from collections import deque

class Node:
	def __init__(self, data):
		self.left = None
		self.right = None
		self.data = data

	# Insert Node
	def insert(self, data):
		if self.data:
			if data < self.data:
				if self.left is None:
					self.left = Node(data)
				else:
					self.left.insert(data)
			elif data > self.data:
				if self.right is None:
					self.right = Node(data)
				else:
					self.right.insert(data)
		else:
			self.data = data

	# Print the Tree
	def PrintTree(self):
		if self.left:
			self.left.PrintTree()

		print( self.data)

		if self.right:
			self.right.PrintTree()

	# Inorder traversal
	# Left -> Root -> Right
	# Time Comeplexity: O(N)
	# Space Complexity: O(N)
	def InorderTraversal(self, root):
		res = []

		if root:
			res = self.InorderTraversal(root.left)
			res.append(root.data)
			res = res + self.InorderTraversal(root.right)

		return res

	# Preorder Traversal
	# Left -> Root -> Right
	# Time Comeplexity: O(N)
	# Space Complexity: O(N)
	def PreorderTraversal(self, root):
		res = []

		if root:
			res.append(root.data)
			res = res + self.PreorderTraversal(root.left)
			res = res + self.PreorderTraversal(root.right)

		return res

	# Postorder traversal
	# Left ->Right -> Root
	# Time Comeplexity: O(N)
	# Space Complexity: O(N)
	def PostorderTraversal(self, root):
		res = []

		if root:
			res = self.PostorderTraversal(root.left)
			res = res + self.PostorderTraversal(root.right)
			res.append(root.data)

		return res

	# Iterative function for inorder tree traversal
	# Time: O(N) 
	# Space: O(H) H = Height
	def InorderTraversal_iterative(self, root):
		current = root
		stack = []
		traversal = []
		
		while True:
			if current is not None:
				stack.append(current)
				current = current.left
			elif(stack):
				current = stack.pop()
				traversal.append(current.data)
				current = current.right
			else:
				break
		
		return traversal

	# Iterative function for preorder tree traversal
	# Time Comeplexity: O(N)
	# Space Complexity: O(N)
	def PreorderTraversal_iterative(self, root):
		if root is None:
			return

		nodeStack = []
		nodeStack.append(root)
		traversal = []
	
		while(len(nodeStack) > 0):
			node = nodeStack.pop()
			traversal.append(node.data)

			if node.right is not None:
				nodeStack.append(node.right)
			if node.left is not None:
				nodeStack.append(node.left)

		return traversal

	# An iterative function to do postorder
	# Time Comeplexity: O(N)
	# Space Complexity: O(N)
	def PostorderTraversal_iterative(self, root):
		if root is None:
			return       
		
		s1 = []
		s2 = []
		traversal = []
		
		s1.append(root)
		
		while s1:
			node = s1.pop()
			s2.append(node)
		
			if node.left:
				s1.append(node.left)
			if node.right:
				s1.append(node.right)
	
		while s2:
			node = s2.pop()
			traversal.append(node.data)

		return traversal

	# Finds if a value is in the binary tree
	def findValue(self, val):
		if val < self.data:
			if self.left is None:
				return str(val)+" Not Found"
		
			return self.left.findValue(val)
		elif val > self.data:
			if self.right is None:
				return str(val)+" Not Found"
			return self.right.findValue(val)
		else:
			return str(self.data) + ' is found'

	# Time: O(N) Space: O(N)
	def invertTree(self, root):
		if root is None:
			return None
		root.left, root.right = \
			self.invertTree(root.right), self.invertTree(root.left)
		return root

	# Time: O(N) Space: O(N)
	def invertTree_iterative(self, root):
		stack = []
		stack.append(root)
		while stack:
			node = stack.pop(-1)
			if node:
				node.left, node.right = node.right, node.left
				stack.append(node.left)
				stack.append(node.right)
		return root

	# Time: O(N) Space: O(N)
	def isValidBST(self, root) -> bool:
		if not root:
			return True

		stack = [(root, -math.inf, math.inf)]
		while stack:
			root, lower, upper = stack.pop()
			if not root:
				continue
			val = root.val
			if val <= lower or val >= upper:
				return False
			stack.append((root.right, val, upper))
			stack.append((root.left, lower, val))
		return True

	# Time: O(N) Space: O(N)
	def min_camera_problem(self, root):
		self.ans = 0
		covered = {None}

		def dfs(node, par = None):
			if node:
				dfs(node.left, node)
				dfs(node.right, node)

				if (par is None and node not in covered or
						node.left not in covered or node.right not in covered):
					self.ans += 1
					covered.update({node, par, node.left, node.right})

		dfs(root)
		return self.ans

	# Time: O(N) Space: O(N)
	def isSymmetric(self, left, right):
			if not left and not right:
				return True
			
			if not left or not right:
				return False
			
			if left.val == right.val:
				check_left = self.isSymmetric(left.left, right.right)
				check_right = self.isSymmetric(left.right, right.left)
				return check_left and check_right
			
			return False

	# Time: O(N) Space: O(N)
	def isSymmetric_iterative(self, left, right):
		if not left or not right:
			return left == right
		
		queue = [[left, right]]
		while queue:
			left, right = queue.pop(0)
			
			if left is None and right is None:
				continue
			if left is None or right is None:
				return False
			if left.val != right.val:
				return False
			queue.append([left.right, right.left])
			queue.append([left.left, right.right])

		return True
	# Time: O(N) Space: O(log(N))
	def path(self, root, path):
		if root:
			path += str(root.val)
			if not root.left and not root.right:  # if reach a leaf
				paths.append(path)  # update paths  
			else:
				path += '->'  # extend the current path
				self.path(root.left, path)
				self.path(root.right, path)

		paths = []
		self.path(root, '')
		return paths

	# Time: O(N) Space: O(N)
	def path_iterative(self, root):
		if not root:
			return []
		
		paths = []
		stack = [(root, str(root.val))]
		while stack:
			node, path = stack.pop()
			if not node.left and not node.right:
				paths.append(path)
			if node.left:
				stack.append((node.left, path + '->' + str(node.left.val)))
			if node.right:
				stack.append((node.right, path + '->' + str(node.right.val)))
		
		return paths

	# Time: O(N) Space: O(log(N))
	def isSameTree(self, p, q):
		# p and q are both None
		if not p and not q:
			return True
		# one of p and q is None
		if not q or not p:
			return False
		if p.val != q.val:
			return False
		return self.isSameTree(p.right, q.right) and \
			   self.isSameTree(p.left, q.left)

	# Time: O(N) Space: Best Case: O(log(N)) worst is O(N)
	def isSameTree_iterative(self, p, q):
		stack = [(p, q)]
		while stack:
			(p, q) = stack.pop()
			if p and q and p.val == q.val:
				stack.extend([
					(p.left,  q.left),
					(p.right, q.right)
				])
			elif p or q:
				return False
		return True

	# Time: O(N) Space: O(log(N))
	def maxDepth(self, root):
		if root is None: 
			return 0 
		else: 
			left_height = self.maxDepth(root.left) 
			right_height = self.maxDepth(root.right) 
			return max(left_height, right_height) + 1 

	# Time: O(N) Space: O(log(N))
	def maxDepth_iteration(self, root):
		stack = []
		if root is not None:
			stack.append((1, root))
		
		depth = 0
		while stack != []:
			current_depth, root = stack.pop()
			if root is not None:
				depth = max(depth, current_depth)
				stack.append((current_depth + 1, root.left))
				stack.append((current_depth + 1, root.right))
		
		return depth

	# Time: O(N) Space: O(log(N))
	def minDepth(self, root):
		if not root: 
			return 0 
		
		children = [root.left, root.right]
		# if we're at leaf node
		if not any(children):
			return 1
		
		min_depth = float('inf')
		for c in children:
			if c:
				min_depth = min(self.minDepth(c), min_depth)
		return min_depth + 1 

	# Time: O(N) Space: O(N)
	def minDepth_iteration(self, root):
		if not root:
			return 0
		else:
			stack, min_depth = [(1, root),], float('inf')
		
		while stack:
			depth, root = stack.pop()
			children = [root.left, root.right]
			if not any(children):
				min_depth = min(depth, min_depth)
			for c in children:
				if c:
					stack.append((depth + 1, c))
		
		return min_depth 

	def height(self, root):
		# An empty tree has height -1
		if not root:
			return -1
		return 1 + max(self.height(root.left), self.height(root.right))
	
	# Time: O(n log n) Space: O(N)
	def isBalanced(self, root):
		# An empty tree satisfies the definition of a balanced tree
		if not root:
			return True

		# Check if subtrees have height within 1. If they do, check if the
		# subtrees are balanced
		return abs(self.height(root.left) - self.height(root.right)) < 2 \
			and self.isBalanced(root.left) \
			and self.isBalanced(root.right)


def main():
	root = Node(27)
	root.insert(14)
	root.insert(35)
	root.insert(10)
	root.insert(19)
	root.insert(31)
	root.insert(42)
	print(root.InorderTraversal(root)) 
	print(root.InorderTraversal_iterative(root))
	print(root.PreorderTraversal(root))
	print(root.PreorderTraversal_iterative(root))
	print(root.PostorderTraversal(root))
	print(root.PostorderTraversal_iterative(root))
	print(root.findValue(10))
	print(root.findValue(100))

if __name__ == "__main__":
	main()