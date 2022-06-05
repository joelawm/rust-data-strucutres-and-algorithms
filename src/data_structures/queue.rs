/*
/data-structures/stack.rs

Queue are linear data strucutres and felxible in size. They're FIFO (First in First out).

*/

pub fn start() {
	println!("Showing a example of a 'queue' in Rust!\n\n");
	let mut queue = Queue::new();

	let mut queue: Queue<isize> = Queue::new();
	queue.enqueue(1);
	let item = queue.dequeue();
	assert_eq!(item, 1);
	assert_eq!(queue.is_empty(), true);

	println!("Added 4 elements to the queue!\n {:#?}", queue);

	queue.remove();

	println!("\nRemoving the first element from the queue!\n {:#?}", queue);

	println!("\nIs the queue empty? - {}", queue.is_empty());
	println!("What is the first element then? - {:?}", queue.peek());
}

struct Queue<T> {
	queue: Vec<T>,
  }
  
  impl<T> Queue<T> {
	fn new() -> Self {
	  Queue { queue: Vec::new() }
	}
  
	fn length(&self) -> usize {
	  self.queue.len()
	}
  
	fn enqueue(&mut self, item: T) {
	  self.queue.push(item)
	}
  
	fn dequeue(&mut self) -> T {
	  self.queue.remove(0)
	}
	fn is_empty(&self) -> bool {
	  self.queue.is_empty()
	}
  
	fn peek(&self) -> Option<&T> {
	  self.queue.first()
	}
  }