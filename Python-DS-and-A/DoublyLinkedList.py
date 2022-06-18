class Node:
	def __init__(self, data):
		self.data = data
		self.next = None
		self.prev = None

class DoublyLinkedList:
	def __init__(self):
		self.head = None

	# Add elements to the array at the beguinning
	def push(self, val):
		NewNode = Node(val)
		NewNode.next = self.head

		if self.head is not None:
			self.head.prev = NewNode
		
		self.head = NewNode

	# Insert elements into the middle of the array
	def insert(self, prev_node, val):
		if prev_node is None:
			return
		
		NewNode = Node(val)
		NewNode.next = prev_node.next
		prev_node.next = NewNode
		NewNode.prev = prev_node

		if NewNode.next is not None:
			NewNode.next.prev = NewNode

	# Add elements to the end of the array
	def append(self, val):
		NewNode = Node(val)
		NewNode.next = None

		if self.head is None:
			NewNode.prev = None
			self.head = NewNode
			return

		last = self.head

		while (last.next is not None):
			last = last.next

		last.next = NewNode
		NewNode.prev = last
		return

	def list_print(self, node):
		while (node is not None):
			print(node.data),
			last = node
			node = node.next

def main():
	dllist = DoublyLinkedList()
	dllist.push(12)
	dllist.append(9)
	dllist.push(8)
	dllist.push(62)
	dllist.append(45)
	dllist.insert(dllist.head.next, 13)
	dllist.list_print(dllist.head)

if __name__ == "__main__":
    main()