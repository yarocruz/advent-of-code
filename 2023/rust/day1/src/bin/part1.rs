fn main() {
    let input = include_str!("input1.txt");
    let output = part1(input);
    dbg!(output);
}

fn part1(input: &str) -> String {
    "something".to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = part1("");
        assert_eq!(result, "4");
    }
}