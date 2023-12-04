use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part2(&file));
}

fn part2(input: &str) -> String {

    let mut total_sum = 0;

    let games: Vec<_> = input
        .lines()
        .map(|line| {
            line
                .split(":")
                .collect::<Vec<_>>()
        })
        .collect();

    for game in games {
        let sets = game[1]
            .trim()
            .split(";")
            .collect::<Vec<_>>();

        let mut blue = 0;
        let mut red = 0;
        let mut green = 0; 

        let mut power_sums = 0;

        for i in 0..sets.len() {
            let set = sets[i]
                .trim()
                .split(" ")
                .collect::<Vec<_>>();

            let mut color_index = 1; 

            for j in 0..set.len() {
                if color_index <= set.len() - 1 {
                    if set[color_index].starts_with("red") {
                        if set[color_index - 1].parse::<i32>().unwrap() > red {
                            red = set[color_index - 1].parse::<i32>().unwrap();
                        } 
                    } 
                    if set[color_index].starts_with("blue") {
                        if set[color_index - 1].parse::<i32>().unwrap() > blue {
                            blue = set[color_index - 1].parse::<i32>().unwrap();
                        } 
                    } 
                    if set[color_index].starts_with("green") {
                        if set[color_index - 1].parse::<i32>().unwrap() > green {
                            green = set[color_index - 1].parse::<i32>().unwrap();
                        } 
                    }  
                    color_index += 2;
                }
                // once we finish with one set, we get the power of the set
                power_sums = red * blue * green; 
            }
            
        }

        total_sum += power_sums;

    }
    total_sum.to_string()
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
        let result = part2(INPUT);
        assert_eq!(result, "2286");
    }
}