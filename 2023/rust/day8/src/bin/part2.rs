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

struct Node {
    value: String,
    children: Vec<Node>,
}

fn part1(input: &str) -> String {
    // parse the first line in the input into vector of chars
    let directions = input
        .lines()
        .take(1)
        .next()
        .unwrap();

    // for every line in the input that starts with AAA = (BBB, CCC)
    // create a node with value AAA
    // add BBB and CCC as children

    let mut nodes = input
        .lines()
        .skip(2)
        .map(|line| {
            let mut parts = line.split(" = ");
            let value = parts.next().unwrap();
            let children = parts.next().unwrap();
            let children = children
                .trim_start_matches("(")
                .trim_end_matches(")")
                .split(", ")
                .map(|child| child.to_string())
                .collect::<Vec<String>>();
            (value.to_string(), children)
        })
        .collect::<HashMap<String, Vec<String>>>();

        
        let mut count = 0;
        let max_iterations = 100000; // Prevents infinite loop

        // find all the nodes that end with A and save them in a vector
        let mut nodes_ending_with_a = nodes
            .keys()
            .filter(|key| key.ends_with("A"))
            .map(|key| key.to_string())
            .collect::<Vec<String>>();

        println!("nodes_ending_with_a: {}", nodes_ending_with_a.len());

        // save all the nodes that end with a in a vector of &str
        let mut current_nodes = nodes_ending_with_a
            .iter()
            .map(|node| node.as_str())
            .collect::<Vec<&str>>();

        println!("current_nodes: {:?}", current_nodes);

        // answer 12737 is too low

        let mut visited = std::collections::HashSet::new();
        //visited.insert(current_nodes.clone());
        
        'outer: while current_nodes.iter().any(|&node| !node.ends_with("Z")) {
            
            for direction in directions.chars() {
                for i in 0..current_nodes.len() {
                    let current_node = current_nodes[i];
                    let next_node = match direction {
                        'L' => &nodes.get(current_node).unwrap()[0],
                        'R' => &nodes.get(current_node).unwrap()[1],
                        _ => panic!("Invalid direction"),
                    };
        
                    current_nodes[i] = next_node;
                }
        
                count += 1;
                println!("Current states: {:?}", current_nodes);

                if visited.contains(&current_nodes) {
                    println!("Already visited this state, terminating");
                    break 'outer;
                }
        
                if current_nodes.iter().all(|&node| node.ends_with("Z")) {
                    println!("All nodes end with Z, terminating");
                    break 'outer;
                }
        
                if count >= max_iterations {
                    println!("Maximum iterations reached, terminating");
                    break 'outer;
                }
            }
            visited.insert(current_nodes.clone());
            
        }

    println!("count: {}", count);

    count.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT1: &str = "LR

11A = (11B, XXX)
11B = (XXX, 11Z)
11Z = (11B, XXX)
22A = (22B, XXX)
22B = (22C, 22C)
22C = (22Z, 22Z)
22Z = (22B, 22B)
XXX = (XXX, XXX)";

    #[test]
    fn it_works() {
        let result = part1(INPUT1);
        assert_eq!(result, "7");
    }
}
