use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    // turn the input into a 2d array like 
    // [[7, 15, 30], [9, 40, 200]]
    let mut races = input
        .lines()
        .map(|line| {
            line.split_whitespace()
                .skip(1)
                .map(|x| x.parse::<usize>().unwrap())
                .collect::<Vec<_>>()
        })
        .collect::<Vec<_>>();

    let mut counts: Vec<u32> = vec![];

    for i in 0..races[0].len() {
        let time = races[0][i];
        let distance = races[1][i];

        let mut count = 0;

        for num in 0..=time {
            let button_hold = time - num;
            let movement = button_hold * num;
            if movement > distance {
                count += 1;
            }
        }
        counts.push(count);
    }

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
        assert_eq!(result, "288");
    }
}
