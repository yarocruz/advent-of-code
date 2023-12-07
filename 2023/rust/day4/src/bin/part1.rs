use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    let mut result: usize = 0;
    // split the input into lines and collect them into a vector
    let cards: Vec<&str> = input.lines().collect();

    /* split the lines and collect the first set of numbers into a vector
        example: The first line contains "Card1 : 41 48 83 86 17 | 83 86  6 31 17  9 48 53"
        we want 41 48 83 86 17 into a vector
     */
    let mut winning_numbers: Vec<Vec<&str>> = vec![vec![]; cards.len()];
    for (i, card) in cards.iter().enumerate() {
        let numbers: Vec<&str> = card.split(":").collect();
        let numbers: Vec<&str> = numbers[1].split("|").collect();
        let numbers: Vec<&str> = numbers[0].trim().split(" ").collect();
        winning_numbers[i] = numbers;
    }

    let mut numbers_you_have: Vec<Vec<&str>> = vec![vec![]; cards.len()];
    for (i, card) in cards.iter().enumerate() {
        let numbers: Vec<&str> = card.split(":").collect();
        let numbers: Vec<&str> = numbers[1].split("|").collect();
        let numbers: Vec<&str> = numbers[1]
            .trim()
            .split(" ")
            .filter(|&x| x != "")
            .collect();
        numbers_you_have[i] = numbers;
    }


    println!("Winning Numbers{:?}", winning_numbers);
    println!("Numbers you have{:?}", numbers_you_have);

    // loop over the numbers you have and check if they are in the winning numbers
    for (i, numbers) in numbers_you_have.iter().enumerate() {
        let mut card_score: usize = 0;
        for number in numbers {
            if winning_numbers[i].contains(number) && card_score < 1 {
                card_score += 1;
            } else if winning_numbers[i].contains(number) && card_score >= 1 {
                card_score = card_score * 2;
            }
        }
        println!("Card {} score: {}", i + 1, card_score);
        result += card_score;
    }

    println!("Result: {}", result);

    result.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11";

    #[test]
    fn it_works() {
        let result = part1(INPUT);
        assert_eq!(result, "13");
    }
}
