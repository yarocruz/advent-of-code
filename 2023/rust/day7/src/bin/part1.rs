use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

/* We need to check types of hands:
From highest to lowest:
    - Five of a kind
    - Four of a Kind
    - Full House: three the same, two the same ex 22233
    - Three of a Kind
    - Two Pairs ex 22335
    - One Pair ex A23A4
    - High Card ex 23456 All are different
*/

fn part1(input: &str) -> String {
    // we want to conver the input into a vector of tuples
    // where the first element is the hand and the second is the bid
    let mut hands: Vec<(&str, &str)> = input
        .lines()
        .map(|line| {
            let mut split = line.split_whitespace();
            let hand = split.next().unwrap();
            let bid = split.next().unwrap();
            (hand, bid)
        })
        .collect();

    println!("{:?}", hands);

    "result".to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "32T3K 765
T55J5 684
KK677 28
KTJJT 220
QQQJA 483";

    #[test]
    fn it_works() {
        let result = part1(INPUT);
        assert_eq!(result, "6440");
    }
}
