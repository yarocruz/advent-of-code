use std::fs;
use regex::Regex;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    let two_d_array: Vec<Vec<char>> = input
        .lines()
        .map(|line| line.chars().collect())
        .collect();

    // find all the contigious numbers in the 2d array
    // for example in the first row we have 467, 114
    // save that number into an array of structs that contain the number and the positions
    // of each of the numbers for example 467 would be (0,0), (0,1), (0,2)
    #[derive(Debug)]
    struct ContigiousNumber {
        number: String,
        positions: Vec<(usize, usize)>,
    }
    let mut contigious_numbers: Vec<ContigiousNumber> = Vec::new();

    for (row_index, row) in two_d_array.iter().enumerate() {
        let mut current_number: String = String::new();
        let mut current_positions: Vec<(usize, usize)> = Vec::new();
        for (col_index, col) in row.iter().enumerate() {
            if col.is_digit(10) {
                current_number.push(*col);
                current_positions.push((row_index, col_index));
            } else {
                if !current_number.is_empty() {
                    contigious_numbers.push(ContigiousNumber {
                        number: current_number.clone(),
                        positions: current_positions.clone(),
                    });
                    current_number.clear();
                    current_positions.clear();
                }
            }
        }
        if !current_number.is_empty() {
            contigious_numbers.push(ContigiousNumber {
                number: current_number.clone(),
                positions: current_positions.clone(),
            });
        }
    }

    // for each number in the contigious numbers array
    // use the positions to look up, down, right, left, and diagonally
    // in the 2d array to check if there are any special characters
    // if we find a symbol then process the current number as a u32 and add it to the total
    let mut total: u32 = 0;
    'outer: for contigious_number in contigious_numbers {
        let mut valid: bool = false;
        for position in contigious_number.positions {
            let mut row_index: usize = position.0;
            let mut col_index: usize = position.1;
            // check up
            if row_index > 0 {
                let mut row_index: usize = position.0;
                let mut col_index: usize = position.1;
                row_index -= 1;
                if is_special_character(two_d_array[row_index][col_index]) {
                    valid = true;
                    break;
                }
            }
            // check down
            if row_index < two_d_array.len() - 1 {
                let mut row_index: usize = position.0;
                let mut col_index: usize = position.1;
                row_index += 1;
                if is_special_character(two_d_array[row_index][col_index]) {
                    valid = true;
                    break;
                }
            }
            // check left
            if col_index > 0 {
                let mut row_index: usize = position.0;
                let mut col_index: usize = position.1;
                col_index -= 1;
                if is_special_character(two_d_array[row_index][col_index]) {
                    valid = true;
                    break;
                }
            }
            // check right
            if col_index < two_d_array[row_index].len() - 1 {
                let mut row_index: usize = position.0;
                let mut col_index: usize = position.1;
                col_index += 1;
                if is_special_character(two_d_array[row_index][col_index]) {
                    valid = true;
                    break;
                }
            }
            // check up left
            if row_index > 0 && col_index > 0 {
                let mut row_index: usize = position.0;
                let mut col_index: usize = position.1;
                row_index -= 1;
                col_index -= 1;
                if is_special_character(two_d_array[row_index][col_index]) {
                    valid = true;
                    break;
                }
            }
            // check up right
            if row_index > 0 && col_index < two_d_array[row_index].len() - 1 {
                let mut row_index: usize = position.0;
                let mut col_index: usize = position.1;
                row_index -= 1;
                col_index += 1;
                if is_special_character(two_d_array[row_index][col_index]){
                    
                    valid = true;
                    break;
                }
            }
            // check down left
            if row_index < two_d_array.len() - 1 && col_index > 0 {
                let mut row_index: usize = position.0;
                let mut col_index: usize = position.1;
                row_index += 1;
                col_index -= 1;
                if is_special_character(two_d_array[row_index][col_index]) {
                    valid = true;
                    break;
                }
            }
            // check down right
            if row_index < two_d_array.len() - 1 && col_index < two_d_array[row_index].len() - 1 {
                let mut row_index: usize = position.0;
                let mut col_index: usize = position.1;  
                row_index += 1;
                col_index += 1;
                if is_special_character(two_d_array[row_index][col_index]) {
                    valid = true;
                    break;
                }
            }
        }
        // find if any character is a special character
        fn is_special_character(character: char) -> bool {
            // if the character is not alphanumeric, a period, or a space
            let re = Regex::new(r"[^a-zA-Z0-9. ]").unwrap();
            re.is_match(&character.to_string())
        }
        if valid {
            total += contigious_number.number.parse::<u32>().unwrap();
        }
    }
    println!("total: {}", total);
    

    total.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..";

    #[test]
    fn it_works() {
        let result = part1(INPUT);
        assert_eq!(result, "4361");
    }
}