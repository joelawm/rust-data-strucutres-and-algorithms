/*
/data-structures/stack.rs

Stacks are linear data strucutres and felxible in size. They're LIFO (Last in First out).

Stacks are useful for balancing problems, task execution, or anything else where the order of execution is important.

*/
pub fn start() {
	let mut stack: Stack<isize> = Stack::new();
	stack.push(1);
	let item = stack.pop();
	assert_eq!(item.unwrap(), 1);
}

struct Stack<T> {
	stack: Vec<T>,
  }
  
  impl<T> Stack<T> {
	fn new() -> Self {
	  Stack { stack: Vec::new() }
	}
  
	fn length(&self) -> usize {
	  self.stack.len()
	}
  
	fn pop(&mut self) -> Option<T> {
	  self.stack.pop()
	}
  
	fn push(&mut self, item: T) {
	  self.stack.push(item)
	}
  
	fn is_empty(&self) -> bool {
	  self.stack.is_empty()
	}
  
	fn peek(&self) -> Option<&T> {
	  self.stack.last()
	}
  }