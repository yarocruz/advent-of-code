use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    // turn the input into a 2d array like
    // the following [[71530] [940200]]
    let races = input
        .lines()
        .map(|line| {
            // we the the numbers 7 15 30 to be 71530
            // and 9 40 200 to be 940200
            // so we need to remove the spaces
            // and then join the numbers together
            // and then parse the string into a number
            line.split_whitespace()
                .skip(1)
                .map(|x| x.parse::<usize>().unwrap())
                .fold(String::new(), |mut acc, x| {
                    acc.push_str(&x.to_string());
                    acc
                })
                .parse::<usize>()
                .unwrap()
        })
        .collect::<Vec<_>>();

    println!("{:?}", races);

    let mut counts: Vec<u32> = vec![];

    
    let time = races[0];
    let distance = races[1];

    let mut count = 0;

    for num in 0..=time {
        let button_hold = time - num;
        let movement = button_hold * num;
        if movement > distance {
            count += 1;
        }
    }
    counts.push(count);
    

    let result = counts.iter().fold(1, |acc, x| acc * x);
    
    result.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "Time:      7  15   30
Distance:  9  40  200";

    #[test]
    fn it_works() {
        let result = part1(INPUT);
        assert_eq!(result, "71503");
    }
}
