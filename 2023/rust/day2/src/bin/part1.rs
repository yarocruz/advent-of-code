use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    const RED:i32 = 12;
    const GREEN:i32 = 13;
    const BLUE:i32 = 14;

    let mut possible_game_count = 0;

    let games: Vec<_> = input
        .lines()
        .map(|line| {
            line
                .split(":")
                .collect::<Vec<_>>()
        })
        .collect();

    for game in games {
        // check how many blue, red, and green we have
        let sets = game[1]
            .trim()
            .split(";")
            .collect::<Vec<_>>();

        let mut blue = 0;
        let mut red = 0;
        let mut green = 0;

        let mut is_possible = true;   

        for i in 0..sets.len() {
            let set = sets[i]
                .trim()
                .split(" ")
                .collect::<Vec<_>>();

            println!("Set {:?}", set);

            let mut color_index = 1; 

            for j in 0..set.len() {
                if color_index <= set.len() - 1 {
                    if set[color_index].starts_with("red") {
                        red = set[color_index - 1].parse::<i32>().unwrap();
                    } 
                    if set[color_index].starts_with("blue") {
                        blue = set[color_index - 1].parse::<i32>().unwrap(); 
                    } 
                    if set[color_index].starts_with("green") {
                        green = set[color_index - 1].parse::<i32>().unwrap();
                    }  
                    //println!("Color Index {}", scores[color_index]);
                    color_index += 2;
                    if blue > BLUE || red > RED || green > GREEN {
                        is_possible = false;
                    }
                } 
                
            }
            println!("red:{} blue:{} green:{}", red, blue, green);

            
        }

        //println!("Color counts blue: {} red: {} gree: {}", blue, red, green);
        
        //color_index = 1;

        // if they are all less than the constant than they are a possible game
        if is_possible {
            let game_id = game[0]
                .split(" ")
                .collect::<Vec<_>>();
            println!("{}", game_id[1]);
            possible_game_count += game_id[1].parse::<i32>().unwrap();
            println!("Game count {}", possible_game_count);
        } 

    }
    possible_game_count.to_string()
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
        assert_eq!(result, "9");
    }
}