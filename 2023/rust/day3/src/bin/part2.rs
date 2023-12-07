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
    #[derive(Debug, Clone)]
    struct GearPosition {
        position: (usize, usize),
        adjascent_part_number: Vec<u32>,
    }

    let mut contigious_numbers: Vec<ContigiousNumber> = Vec::new();

    // add an array of gear positions
    let mut gear_positions: Vec<GearPosition> = vec![
        GearPosition {
            position: (0, 0),
            adjascent_part_number: Vec::new(),
        }
    
    ];

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
    for contigious_number in contigious_numbers {
        'outer: for position in contigious_number.positions {
            let mut row_index: usize = position.0;
            let mut col_index: usize = position.1;
    
            // check in all directions (up, down, left, right, up-left, up-right, down-left, down-right)
            for (delta_row, delta_col) in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)] {
                if let Some((new_row, new_col)) = check_position(row_index, col_index, delta_row, delta_col, &two_d_array) {
                    let number = contigious_number.number.parse::<u32>().unwrap();
                    let mut found = false;
    
                    for gear_position in &mut gear_positions {
                        if gear_position.position == (new_row, new_col) {
                            gear_position.adjascent_part_number.push(number);
                            found = true;
                            break;
                        }
                    }
    
                    if !found {
                        gear_positions.push(GearPosition {
                            position: (new_row, new_col),
                            adjascent_part_number: vec![number],
                        });
                    }
    
                    break 'outer;
                }
            }
        }
    }

    // Utility function to check a position in a direction and return the new position if valid
    fn check_position(row: usize, col: usize, delta_row: isize, delta_col: isize, array: &Vec<Vec<char>>) -> Option<(usize, usize)> {
        let new_row = row as isize + delta_row;
        let new_col = col as isize + delta_col;

        if new_row >= 0 && new_col >= 0 && new_row < array.len() as isize && new_col < array[row].len() as isize {
            let new_row = new_row as usize;
            let new_col = new_col as usize;

            if is_special_character(array[new_row][new_col]) {
                return Some((new_row, new_col));
            }
        }

        None
    }

    // find if any character is a *
    fn is_special_character(character: char) -> bool {
        // if the character is not alphanumeric, a period, or a space
        let re = Regex::new(r"\*").unwrap();
        re.is_match(&character.to_string())
    }
    // for each gear position in the gear_positions array
    // if the adjascent_part_number arrary has exactly 2 numbers
    // and if we haven't seen this position before
    // then multiply the two numbers together and add it to the total

    for gear_position in &gear_positions {
        let current_position = gear_position.position;
        if gear_position.adjascent_part_number.len() == 2 {
            total += gear_position.adjascent_part_number[0] * gear_position.adjascent_part_number[1];
        }
    }

    println!("gear_positions: {:?}", gear_positions);

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
        assert_eq!(result, "467835");
    }
}