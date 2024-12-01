use std::fs;
use std::collections::HashSet;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    let field = convert_input(input);

    let start_position = find_start(&field);
    /* From the start position look up, down, left, and or right
       and check to see if it's the appropriate pipe, keep a count
       variable that will count, a visited hash as well. once we finish
       going around a loop, we return the count
     */
    let mut current_position = start_position;
    // let's keep track of the visited positions
    let mut visited = HashSet::new();
    visited.insert(current_position);

    loop {
        let (row, col) = current_position;
        let current = &field[row][col];
        let next = match current.as_str() {
            "S" => (row + 1, col),
            "L" => (row, col + 1),
            "J" => (row, col - 1),
            "-" => (row, col + 1),
            "|" => (row + 1, col),
            "+" => (row + 1, col),
            _ => break,
        };

        if visited.contains(&next) {
            break;
        }

        visited.insert(next);
        current_position = next;
    }
    
    "result".to_string()
}

fn convert_input(input: &str) -> Vec<Vec<String>> {
    let field = input
        .lines()
        .map(|line| line.split("").map(|c| c.to_string()).collect::<Vec<String>>())
        .collect::<Vec<Vec<String>>>();

    field
}

fn find_start(field: &Vec<Vec<String>>) -> (usize, usize) {
    let mut result = (0, 0); 
    for row in 0..field.len() {
        for col in 0..field[row].len() {
            if field[row][col] == "S" {
                result = (row, col);
            }
        }
    }
    result
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = ".....
.S-7.
.|.|.
.L-J.
.....";

    #[test]
    fn it_works() {
        let result = part1(INPUT);
        assert_eq!(result, "4");
    } 
}
