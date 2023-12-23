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

    let mut result: i32 = 0;

    for sequence in sequences {
        let mut temp: i32 = 0;

        let mut subsequence = generate_subsequence(&sequence);
        let mut sub_history = Vec::new();
        sub_history.push(sequence.clone());

        // while all the numbers inside one subsequence are not the same
        // keep generating subsequences
        while subsequence
            .split(" ")
            .map(|x| x.parse::<i32>().unwrap())
            .collect::<Vec<i32>>()
            .iter()
            .all(|&x| x == subsequence.split(" ")
            .map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>()[0]) == false {
            sub_history.push(subsequence.clone());
            subsequence = generate_subsequence(&subsequence);
        }

        sub_history.push(subsequence.clone());
        sub_history.reverse();
        println!("sub_history: {:?}", sub_history);
        // for each sequence in the sub_history
        // we want to get the last number in the sequence
        // and add it to the temp variable
        for sequence in sub_history.iter() {
            let first_number = sequence
                .split(" ")
                .next()
                .unwrap()
                .parse::<i32>()
                .unwrap();

            // subtract each first number from the sequence by the next first number in
            println!("first_number: {}", first_number); 
            temp = first_number - temp;
            println!("temp: {}", temp);
        }

        //println!("temp: {}", temp);

        println!("subsequence: {}", subsequence);

        result += temp;
        // reset temp
        temp = 0;
    }

    // 1719430968 came out as too low
    println!("result: {}", result);

    result.to_string()
}

fn generate_subsequence(sequence: &str) -> String {
    /*
        based on the sequence, we want to generate a list of subsequences
        for example, if the sequence is "0 3 6 9 12 15"
        we want to generate the following subsequences:
        [3, 3, 3, 3, 3]
        then after that [0,0,0,0]
        we want to return back the following vector of vectors:
        [[0, 3, 6, 9, 12, 15],[3, 3, 3, 3, 3], [0,0,0,0]]
     */
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

    // join the subsequences vector into a string
    // and return it
    subsequences.join(" ")
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
        assert_eq!(result, "2");
    } 
}
