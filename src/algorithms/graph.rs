// Depth first search
// Breadth first serach

pub struct Node<'a, T> {
	value: T,
	edges: Vec<&'a Node<'a, T>>
  }
  
  impl<'a, T: PartialEq> Node<'a, T> {
	pub fn new(value: T) -> Self {
	  Self {
		value,
		edges: Vec::new()
	  }
	}
  }
  
  pub struct Graph<'a, T> {
	nodes: Vec<Node<'a, T>>
  }
  
  impl<'a, T: PartialEq> Graph<'a, T> {
	pub fn new() -> Self {
	  Self {
		nodes: Vec::new()
	  }
	}
  
	pub fn add_node(&mut self, value: T) {
	  self.nodes.push(Node::new(value))
	}
	
	pub fn get_node(&self, value: T) -> Option<&Node<T>> {
	  self.nodes.iter().find(|node| node.value == value)
	}
  
	pub fn add_edge(&mut self, value_a: T, value_b: T) {
	  let ref mut node_a = self.get_node(value_a);
	  let mut node_b = self.get_node(value_b);
	  match (node_a, node_b) {
		(Some(a), Some(b)) => {
		  a.edges.push(b);
		},
		_ => panic!("Node not found!")
	  }
	}
  }

/////////// DFS
use std::vec;

struct Tree<T> {
    children: Vec<Tree<T>>,
    value: T
}

impl<T> Tree<T> {
    pub fn new(value: T) -> Self{
        Tree{
            children: vec![],
            value
        }
    }

    pub fn dfs<F: Fn(&T)>(&self, f: F) {
       self.dfs_helper(&f);
    }

    fn dfs_helper<F: Fn(&T)>(&self, f: &F) {
        (f)(&self.value);
        for child in &self.children {
            child.dfs_helper(f);
        }
    }
}


fn main() {
    let t: Tree<i32> = Tree {
        children: vec![
            Tree {
                children: vec![
                    Tree {
                        children: vec![],
                        value: 14
                    }
                ],
                value: 28
            },
            Tree {
                children: vec![],
                value: 80
            }
        ],
        value: 50
    };

    t.dfs(|node| { println!("{}", node); });
}


/// BFS
use std::collections::VecDeque;

struct Tree<V> {
    children: Vec<Tree<V>>,
    value: V
}

impl<V> Tree<V> {
    fn bfs(&self, f: impl Fn(&V)) {
        let mut q = VecDeque::new();
        q.push_back(self);

        while let Some(t) = q.pop_front() {
            (f)(&t.value);
            for child in &t.children {
                q.push_back(child);
            }
        }
    }
}

fn main() {
    let t = Tree {
        children: vec![
            Tree {
                children: vec![
                    Tree { children: vec![], value: 5 },
                    Tree { children: vec![], value: 6 }
                ],
                value: 2
            },
            Tree { children: vec![], value: 3 },
            Tree { children: vec![], value: 4 },
        ],
        value: 1
    };
    t.bfs(|v| println!("{}", v));
}