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

//    let mut new_seeds: Vec<u64> = Vec::new();

//    for i in 0..seeds.len() {
//        if i % 2 == 0 {
//             let start = seeds[i];
//             let end = start + seeds[i + 1] - 1;

//             for j in start..=end {
//                 new_seeds.push(j);
//             }
//        }
//     }


    // let mut values: Vec<Vec<u64>> = Vec::new();

    let mut min_location = u64::MAX;

    for i in (0..seeds.len()).step_by(2) {
        let start = seeds[i];
        let end = start + seeds[i + 1] - 1;

        let mut ranges = vec![(start, end)];

        for map in &maps {
            let mut new_ranges = Vec::new();

            for &(start, end) in &ranges {
                let mut any_transformed = false;
                for m in map {
                    let transformed_range = transform_range(start, end, m[1], m[0], m[2]);
                    if let Some((new_start, new_end)) = transformed_range {
                        new_ranges.push((new_start, new_end));
                        any_transformed = true;
                    }
                }

                if !any_transformed {
                    new_ranges.push((start, end));
                }
            }
            println!("{:?}", new_ranges);

            ranges = new_ranges;
        }

        for (start, end) in ranges {
            min_location = min_location.min(start).min(end);
            println!("{}", min_location.min(start).min(end));
        }
    }

    // for every vector in the values vector, we want look at the last value
    // and and check which one is the smallest
    // let mut min = 0;
    // let mut min_index = 0;
    // for (i, v) in values.iter().enumerate() {
    //     let last = v.last().unwrap();
    //     if i == 0 {
    //         min = *last;
    //         min_index = i;
    //     } else {
    //         if *last < min {
    //             min = *last;
    //             min_index = i;
    //         }
    //     }
    // }

    min_location.to_string()
}

fn transform_range(start: u64, end: u64, source: u64, dest: u64, len: u64) -> Option<(u64, u64)> {
    if start >= source + len - 1 || end <= source {
        // No overlap with the map range
        return None;
    }

    let effective_start = start.max(source);
    let effective_end = end.min(source + len - 1);

    let shift = if dest < source {
        dest as i64 - source as i64
    } else {
        dest as i64 - source as i64
    };

    Some(((effective_start as i64 + shift) as u64, (effective_end as i64 + shift) as u64))
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
        assert_eq!(result, "46");
    }
}
