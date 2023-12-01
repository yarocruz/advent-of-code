fn main() {
    let input = include_str!("input1.txt");
    let output = part2(input);
    dbg!(output);
}

fn part2(input: &str) -> String {
    "banana".to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = part2("");
        assert_eq!(result, "4");
    }
}