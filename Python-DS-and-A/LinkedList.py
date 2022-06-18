class Node:
	def __init__(self, val=None):
		self.data = val
		self.next = None

class LinkedList:
	def __init__(self):
		self.head = None

	def list_print(self):
		printval = self.head
		while printval is not None:
			print (printval.data)
			printval = printval.next

	# Adds to the beginning of the list
	def push(self, newdata):
		NewNode = Node(newdata)

		# Update the new nodes next val to existing node
		NewNode.next = self.head
		self.head = NewNode

	# Insert into the middle of a list
	def insert(self, middle_node, newdata):
		if middle_node is None:
			print("The mentioned node is absent")
			return
		
		NewNode = Node(newdata)
		NewNode.next = middle_node.next
		middle_node.next = NewNode

	# Function to remove node
	def remove(self, Removekey):
		HeadVal = self.head
		if (HeadVal is not None):
			if (HeadVal.data == Removekey):
				self.head = HeadVal.next
				HeadVal = None
				return
				
		while (HeadVal is not None):
			if HeadVal.data == Removekey:
				break
			prev = HeadVal
			HeadVal = HeadVal.next
			
			
		if (HeadVal == None):
			return
			
		prev.next = HeadVal.next
		HeadVal = None

	# Time: O(n+m) Space: O(1)
	def mergeTwoSortedLists(self, l1, l2):
		# maintain an unchanging reference to node ahead of the return node.
		prehead = Node(-1)

		prev = prehead
		while l1 and l2:
			if l1.val <= l2.val:
				prev.next = l1
				l1 = l1.next
			else:
				prev.next = l2
				l2 = l2.next            
			prev = prev.next

		# At least one of l1 and l2 can still have nodes at this point, so connect
		# the non-null list to the end of the merged list.
		prev.next = l1 if l1 is not None else l2

		return prehead.next


def main():
	list = LinkedList()
	list.push("Mon")
	list.push("Tue")
	list.push("Wed")
	list.push("Thu")
	list.remove("Tue")
	list.list_print()

if __name__ == "__main__":
	main()