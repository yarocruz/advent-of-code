use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    // for each line in the input
    // push into a vector of strings
    let sequences = input
        .lines()
        .map(|line| line.to_string())
        .collect::<Vec<String>>();

    let subsequence = generate_subsequence(&sequences[0]);
    println!("{:?}", subsequence);

    "count".to_string()
}

fn generate_subsequence(sequence: &str) -> Vec<String> {
    let mut subsequences = Vec::new();
    let mut history = sequence.split(" ").collect::<Vec<&str>>();

    // for each number in the history we want to next from the previous number
    // for example, if the history is [0, 3, 6, 9, 12, 15]
    // we subtract 3 - 0 = 3, then 6 - 3 = 3, then 9 - 6 = 3, an so on
    // we push each result into the subsequences vector
    for i in 0..history.len() {
        //let mut subsequence = Vec::new();
        let mut previous = history[i].parse::<i32>().unwrap();
        
        if i != history.len() - 1 {
            let current = history[i + 1].parse::<i32>().unwrap();
            let next = current - previous;
            subsequences.push(next.to_string());
        }
    }

    subsequences
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45";

    #[test]
    fn it_works() {
        let result = part1(INPUT);
        assert_eq!(result, "114");
    } 
}
