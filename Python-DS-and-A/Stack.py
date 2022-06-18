class Stack:
	def __init__(self):
		self.stack = []

	def add(self, val):
		# use list append method to add element
		if val not in self.stack:
			self.stack.append(val)
			return True
		else:
			return False

		# Use peek to look at the top of the stack

	def peek(self):
		return self.stack[-1]

	# Use list pop method to remove element
	def remove(self):
		if len(self.stack) <= 0:
			return ("No element in the Stack")
		else:
			return self.stack.pop()

	# Time Complexity: O(1)
	def top(self) -> int:
		return self.stack[-1][0]
		
	# Time Complexity: O(1)
	def getMin(self) -> int:
		return self.stack[-1][1]

def main():
	AStack = Stack()
	AStack.add("Mon")
	AStack.add("Tue")
	AStack.peek()
	print(AStack.peek())
	AStack.add("Wed")
	AStack.add("Thu")
	print(AStack.peek())

	AStack = Stack()
	AStack.add("Mon")
	AStack.add("Tue")
	AStack.add("Wed")
	AStack.add("Thu")
	print(AStack.remove())
	print(AStack.remove())

if __name__ == "__main__":
	main()