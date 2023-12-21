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
        let max_iterations = 10; // Prevents infinite loop

        // find all the nodes that end with A and save them in a vector
        let mut nodes_ending_with_a = nodes
            .keys()
            .filter(|key| key.ends_with("A"))
            .map(|key| key.to_string())
            .collect::<Vec<String>>();

        println!("nodes_ending_with_a: {}", nodes_ending_with_a.len());

        let mut current1 = &nodes_ending_with_a[0];
        let mut current2 = &nodes_ending_with_a[1];
        let mut current3 = &nodes_ending_with_a[2];
        let mut current4 = &nodes_ending_with_a[3];
        let mut current5 = &nodes_ending_with_a[4];
        let mut current6 = &nodes_ending_with_a[5];
        
        while current1.ends_with("Z") == false || current2.ends_with("Z") == false
            || current3.ends_with("Z") == false || current4.ends_with("Z") == false
            || current5.ends_with("Z") == false || current6.ends_with("Z") == false {
            for direction in directions.chars() {
                println!("direction: {}", direction);
                let next_node = match direction {
                    'L' => &nodes.get(current1).unwrap()[0],
                    'R' => &nodes.get(current1).unwrap()[1],
                    _ => panic!("Invalid direction"),
                };
                let next_node1 = match direction {
                    'L' => &nodes.get(current2).unwrap()[0],
                    'R' => &nodes.get(current2).unwrap()[1],
                    _ => panic!("Invalid direction"),
                };
                let next_node2 = match direction {
                    'L' => &nodes.get(current3).unwrap()[0],
                    'R' => &nodes.get(current3).unwrap()[1],
                    _ => panic!("Invalid direction"),
                };
                let next_node3 = match direction {
                    'L' => &nodes.get(current4).unwrap()[0],
                    'R' => &nodes.get(current4).unwrap()[1],
                    _ => panic!("Invalid direction"),
                };
                let next_node4 = match direction {
                    'L' => &nodes.get(current5).unwrap()[0],
                    'R' => &nodes.get(current5).unwrap()[1],
                    _ => panic!("Invalid direction"),
                };
                let next_node5 = match direction {
                    'L' => &nodes.get(current6).unwrap()[0],
                    'R' => &nodes.get(current6).unwrap()[1],
                    _ => panic!("Invalid direction"),
                };
                let next_node6 = match direction {
                    'L' => &nodes.get(current6).unwrap()[0],
                    'R' => &nodes.get(current6).unwrap()[1],
                    _ => panic!("Invalid direction"),
                };
        
                current1 = next_node;
                current2 = next_node1;
                current3 = next_node2;
                current4 = next_node3;
                current5 = next_node4;
                current6 = next_node5;
                println!("current1: {}", current1);
                println!("current2: {}", current2);
                println!("current3: {}", current3);
                println!("current4: {}", current4);
                println!("current5: {}", current5);
                println!("current6: {}", current6);
                count += 1;
            }
        
        }
        
        if count >= max_iterations {
            println!("Maximum iterations reached, terminating");
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
        assert_eq!(result, "6");
    }
}
