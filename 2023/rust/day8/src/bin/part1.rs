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

        let mut current = "AAA";
        let mut count = 0;
        let max_iterations = 100000; // Prevents infinite loop
        
        while current != "ZZZ" && count < max_iterations {
            for direction in directions.chars() {
                println!("direction: {}", direction);
                let next_node = match direction {
                    'L' => &nodes.get(current).unwrap()[0],
                    'R' => &nodes.get(current).unwrap()[1],
                    _ => panic!("Invalid direction"),
                };
        
                current = next_node;
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
