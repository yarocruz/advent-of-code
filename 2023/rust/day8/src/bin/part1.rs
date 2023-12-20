use std::fs;
use std::collections::HashMap;
use std::rc::Rc;
use std::cell::RefCell;
use std::borrow::Borrow;
use std::cell::Ref;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

/*
we want to create a linked list of nodes
*/

type NodeLink = Option<Rc<RefCell<Node>>>;

struct Node {
    pub value: String,
    pub left: NodeLink,
    pub right: NodeLink,
}

impl Node {
    fn new(value: String) -> Rc<RefCell<Self>> {
        Rc::new(RefCell::new(Node {
            value,
            left: None,
            right: None,
        }))
    }
}

fn part1(input: &str) -> String {
    // parse the first line in the input into vector of chars
    let directions = input
        .lines()
        .take(1)
        .next()
        .unwrap();

    // after the empty line, we have the following format:
    // AAA = (BBB, CCC)
    // BBB = (DDD, EEE)
    // each of these can be represented as node with left and right children
    // create linked list of nodes

    let tree = build_tree(&input.lines().skip(2).collect::<Vec<&str>>());
    let mut count = 0;

    // Example of accessing a node and its children
    if let Some(node_link_option) = tree.get("AAA") {
        if let Some(node_rc) = node_link_option {
            let node_borrow: Ref<Node> = node_rc.as_ref().borrow();
            while node_borrow.value != "ZZZ" {
                count += 1;
                for direction in directions.chars() {
                    match direction {
                        'L' => {
                            if let Some(left_node) = node_borrow.left {
                                if let Some(left) = left_node.as_ref().borrow().left {
                                    node_borrow = left.as_ref().borrow();
                                }
                                
                            }
                        }
                        'R' => {
                            if let Some(right_node) = node_borrow.right {
                                if let Some(right) = right_node.as_ref().borrow().right {
                                    node_borrow = right.as_ref().borrow();
                                }
                            }
                        }
                        _ => panic!("Unknown direction"),
                    }
                }
            }
            println!("AAA: {}", node_borrow.value);
        }
    }

    println!("count: {}", count);

    "result".to_string()
}

fn build_tree(input: &[&str]) -> HashMap<String, NodeLink> {
    let mut nodes = HashMap::new();

    for line in input {
        let parts: Vec<&str> = line.split(" = (").collect();
        let value = parts[0].to_string();
        let children: Vec<&str> = parts[1].trim_end_matches(')').split(", ").collect();

        // Ensure that nodes are inserted as Some(Rc<RefCell<Node>>)
        let left_node = nodes.entry(children[0].to_string())
                            .or_insert_with(|| Some(Node::new(children[0].to_string())))
                            .clone();
        let right_node = nodes.entry(children[1].to_string())
                             .or_insert_with(|| Some(Node::new(children[1].to_string())))
                             .clone();

        let parent_node = Node::new(value);
        parent_node.borrow_mut().left = left_node;
        parent_node.borrow_mut().right = right_node;

        nodes.insert(parts[0].to_string(), Some(Rc::clone(&parent_node)));
    }

    nodes
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT1: &str = "RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)";

const INPUT2: &str = "LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)";

    #[test]
    fn it_works() {
        let result = part1(INPUT1);
        assert_eq!(result, "2");
    }
    #[test]
    fn it_works2() {
        let result = part1(INPUT2);
        assert_eq!(result, "6");
    }
}
