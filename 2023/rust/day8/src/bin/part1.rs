use std::fs;
use std::collections::HashMap;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

/*
we want to create a linked list of nodes

A Node should look like the following:

*/

struct Node<'a> {
    value: &'a str,
    left: Option<Box<Node<'a>>>,
    right: Option<Box<Node<'a>>>,
}

impl Node<'_> {
    fn new(value: &str) -> Node {
        Node {
            value,
            left: None,
            right: None,
        }
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
    // and so on... we want to take the AAA as a new Node, and then the BBB as the left node and CCC as the right node
    // then we want to take the BBB as a new Node, and then the DDD as the left node and EEE as the right node
    // and so on...

    for line in input.lines().skip(2) {
        let mut split = line.split(" = ");
        let node = split.next().unwrap();

        let children = split.next().unwrap();
        let mut children = children.split(", ");
        let left = children.next().unwrap();
        let right = children.next().unwrap();

        println!("node: {}, left: {}, right: {}", node, left, right);
    }

    "result".to_string()
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
