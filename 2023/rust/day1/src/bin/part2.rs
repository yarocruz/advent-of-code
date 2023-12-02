use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part2(&file));
}

fn part2(input: &str) -> String {
  let output = input
    .lines()
    .map(process_line)
    .filter_map(|s| {
      println!("{}", s);
      s.parse::<u32>().ok()
    })
    .sum::<u32>();

  output.to_string()
}

fn process_line(line: &str) -> String {
  
  let mut index = 0;
  let line_iter = std::iter::from_fn(move || {
    let reduced_line = &line[index..];

    let result = if reduced_line.starts_with("one") {
      
      Some('1')
    } else if reduced_line.starts_with("two") {
      
      Some('2') 
    } else if reduced_line.starts_with("three") {
     
      Some('3') 
    } else if reduced_line.starts_with("four") {
      
      Some('4') 
    } else if reduced_line.starts_with("five") {
      
      Some('5') 
    } else if reduced_line.starts_with("six") {
     
      Some('6') 
    } else if reduced_line.starts_with("seven") {
      
      Some('7') 
    } else if reduced_line.starts_with("eight") {

      Some('8') 
    } else if reduced_line.starts_with("nine") {
      Some('9') 
    } else {
      let result = reduced_line.chars().next();
      
      result
    };
    index += 1;
    result
  });

  let mut it = line_iter
    .filter_map(|character| character.to_digit(10));

  let first = it.next().expect("should be a number");
  
  match it.last() {
    Some(num) => format!("{first}{num}"),
    None => format!("{first}{first}")
  }

  // println!("{}{}", first, last);

  // format!("{first}{last}")
 
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen";

    #[test]
    fn it_works() {
        let result = part2(INPUT);
        assert_eq!(result, "281");
    }
}
