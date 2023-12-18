use std::fs;
use std::collections::HashMap;

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

    We can probably use a merge sort algorith the rank the hands
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

    hands.sort_by(|a, b| compare_hands(b.0, a.0));

    println!("{:?}", hands);

    let mut result = 0;
    
    for (i, h) in hands.iter().enumerate() {
        result += (i + 1) * h.1.parse::<usize>().unwrap();
    }

    result.to_string()
}

fn compare_hands(a: &str, b: &str) -> std::cmp::Ordering {
    let rank_map = card_rank_map();
    let a_type = hand_type(a);
    let b_type = hand_type(b);

    if a_type != b_type {
        return a_type.cmp(&b_type);
    }

    a.chars().zip(b.chars()).find_map(|(ac, bc)| {
        let a_rank = rank_map[&ac];
        let b_rank = rank_map[&bc];
        if a_rank != b_rank {
            Some(b_rank.cmp(&a_rank))
        } else {
            None
        }
    }).unwrap_or(std::cmp::Ordering::Equal)
}

fn card_rank_map() -> HashMap<char, i32> {
    let ranks = "AKQJT98765432J";
    ranks.chars().enumerate().map(|(i, c)| (c, -(i as i32))).collect()
}

fn hand_type(hand: &str) -> i32 {
    let mut counts = HashMap::new();
  
    for c in hand.chars().take(5) {
        *counts.entry(c).or_insert(0) += 1;
    }

     // iterate through the counts hashmap and check if there is a j key
    // if there is a j, add the value of the j to the highest counted key
    // and remove the joker from the counts 
    // for example the hashmap {'T': 1, 'J': 1, '5': 3} would become {'T': 1, '5': 4}

    // check if all the keys in the hashmap are all jokers
     if !counts.keys().all(|k| *k == 'J') {
        if counts.contains_key(&'J') {
            let joker_count = counts[&'J'];
    
            // let highest_count = counts.values().max().unwrap();
            // let highest_key = counts.iter().find(|(_, v)| *v == highest_count).unwrap().0;
    
            // get highest count but exclude the j card
            let highest_count = counts.iter().filter(|(k, _)| **k != 'J').max_by_key(|(_, v)| *v).unwrap().1;
            let highest_key = counts.iter().filter(|(k, _)| **k != 'J').max_by_key(|(_, v)| *v).unwrap().0;
    
            counts.insert(*highest_key, highest_count + joker_count);
            counts.remove(&'J');
        }
     }
    
    match counts.values().collect::<Vec<&i32>>()[..] {
        [5] => 1,
        [1, 4] | [4, 1] => 2,
        [2, 3] | [3, 2] => 3,
        [1, 1, 3] | [1, 3, 1] | [3, 1, 1] => 4,
        [1, 2, 2] | [2, 1, 2] | [2, 2, 1] => 5,
        [1, 1, 1, 2] | [1, 1, 2, 1] | [1, 2, 1, 1] | [2, 1, 1, 1] => 6,
        _ => 7,
    }
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
        assert_eq!(result, "5905");
    }
}
