use std::fs;

fn main() {
    let file = fs::read_to_string("./input.txt").unwrap();
    println!("{}", part1(&file));
}

fn part1(input: &str) -> String {
    // parse the seeds, which is the first line 'seeds: 79 14 55 13'
    let seeds: Vec<u64> = input
        .lines()
        .next()
        .unwrap()
        .split(": ")
        .nth(1)
        .unwrap()
        .split(" ")
        .map(|s| s.parse().unwrap())
        .collect();

    // for the maps, which look like the following:
    // seed-to-soil map:
    // 50 98 2
    // 52 50 48
    // we want the first map to be a vector of vectors that looks like the following
    // [[50, 98, 2], [52, 50, 48]]
    // we want to do this for each map
    let sections: Vec<&str> = input.split("\n\n").collect(); 
   
    //println!("{:?}", sections);

    let maps:Vec<Vec<Vec<u64>>> = sections
        .iter()
        .skip(1) // Skip the first line, which is the seeds
        .map(|section| {
            section
                .lines()
                .skip(1) // Skip the title of each map section
                .map(|row| {
                    row.split_whitespace()
                        .map(|s| s.parse::<u64>().unwrap())
                        .collect::<Vec<u64>>()
                })
                .collect::<Vec<Vec<u64>>>()
        })
        .collect();

    let mut values: Vec<Vec<u64>> = Vec::new();

    for seed in seeds {
        let mut s = seed;
        let mut corresponding_values: Vec<u64> = vec![s];
        for map in &maps {
            
            for m in map {
                // get the three values from the map
                
                let dest = m[0];
                let source = m[1];
                let len = m[2];
                if s <= (source + len - 1) && s >= source {
                    //corresponding_values.push(seed + dest - source);
                    if (dest < source) {
                        s = s - (source - dest);
                        break;
                    } else {
                        s = s + (dest - source);
                        break;
                    } 
                }
            }
            corresponding_values.push(s);
        }
        values.push(corresponding_values);
    }

    // for every vector in the values vector, we want look at the last value
    // and and check which one is the smallest
    let mut min = 0;
    let mut min_index = 0;
    for (i, v) in values.iter().enumerate() {
        let last = v.last().unwrap();
        if i == 0 {
            min = *last;
            min_index = i;
        } else {
            if *last < min {
                min = *last;
                min_index = i;
            }
        }
    }

    min.to_string()
}

#[cfg(test)]
mod tests {
    use super::*;

    const INPUT: &str = "seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4";

    #[test]
    fn it_works() {
        let result = part1(INPUT);
        assert_eq!(result, "35");
    }
}
