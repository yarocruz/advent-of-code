use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    let field = convert_input(input);
    println!("{:?}", field);

    let start_position = find_start(&field);
    println!("{:?}", start_position);
    
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
