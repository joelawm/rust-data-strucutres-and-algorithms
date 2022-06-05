/*
/data-structures/linked_list.rs

This is a example of a singly linked list.

*/
pub fn start() {
	println!("Showing a example of a 'singily linked list' in Rust!\n\n");
	// Create a new singly linked list
	let mut linked_list = List::<i32>::new();

	linked_list.push(16);
	linked_list.push(15);
	linked_list.push(19);
	linked_list.push(20);

	println!("Pushed 4 elements to the list!\n {:#?}", linked_list);

	linked_list.pop();

	println!("\nRemoving the first element from the list!\n {:#?}", linked_list);
}

#[derive(Debug)]
struct Node<T> {
    data: T,
    next: Option<Box<Node<T>>>,
}

#[derive(Debug)]
struct List<T> {
    head: Option<Box<Node<T>>>,
}

impl<T> List<T> {
    fn new() -> List<T> {
        List { head: None }
    }

    fn push(&mut self, elem: T) {
		self.head = Some(Box::new(Node {data: elem, next: self.head.take()}));
    }
    
    fn pop(&mut self) -> Option<T> {
        match self.head.take() {
            None => None,
            Some(mut head) => {
                self.head = head.next.take();
                Some(head.data)
            }
        }
    }
}