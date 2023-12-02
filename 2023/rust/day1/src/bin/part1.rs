use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    // we need to split by each line
    let lines: Vec<_> = input
        .split("\n")
        .map(|s| s)
        .collect();
    // vec we're we will save the concat digits
    let mut c_values: Vec<String> = vec![];
    // then split each item
    for line in &lines {
        let chars: Vec<_> = line
            .split("")
            .map(|item| item.trim())
            .collect();

        let mut digits = "".to_owned();

        'outer: for char in &chars {
            for c in char.chars() {
                if c.is_numeric() {
                    digits += char;
                    break 'outer;
                }
            }
        }
        'outer: for char in chars.iter().rev() {
            for c in char.chars() {
                if c.is_numeric() {
                    digits += char;
                    break 'outer;
                }
            }
        }

        c_values.push(digits);

    }
        
     let result = c_values
        .iter()
        .map(|item| {
            item.parse::<u32>().unwrap()
        })
        .sum::<u32>();
    result.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "1abc2
pqr3stu8vwx
a1b2c3d4e5f
treb7uchet";

    #[test]
    fn it_works() {
        let result = part1(INPUT);
        assert_eq!(result, "142");
    }
}