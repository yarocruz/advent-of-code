use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    let output: Vec<_> = input
        .lines()
        // .map(|line| {
        //     line
        //         .split(":")
        //         .map(|m| m);
        // })
        .collect();
    println!("{:?}", output);
    "fail".to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green";

    #[test]
    fn it_works() {
        let result = part1(INPUT);
        assert_eq!(result, "8");
    }
}
