class Queue:
	def __init__(self):
		self.queue = list()

	# Insert method to add element
	def add(self, val):
		if val not in self.queue:
			self.queue.insert(0, val)
			return True

		return False

	def size(self):
		return len(self.queue)

	def remove(self):
		if len(self.queue) > 0:
			return self.queue.pop()
		return ("No Elements in the Queue")

def main():
	TheQueue = Queue()
	TheQueue.add("Mon")
	TheQueue.add("Tue")
	TheQueue.add("Wed")
	print(TheQueue.remove())
	print(TheQueue.remove())
	print(TheQueue.size())

if __name__ == "__main__":
    main()