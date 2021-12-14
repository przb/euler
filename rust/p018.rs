/**
By starting at the top of the triangle below and moving to adjacent numbers on the row below,
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below: (in the text file)

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route.
However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot
be solved by brute force, and requires a clever method! ;o)

 */
use std::fs;

fn parse_file_contents(filename: &str) -> Vec<Vec<u8>> {
    let contents = fs::read_to_string(filename).expect("Something went wrong reading the file");

    let mut parsed_contents: Vec<Vec<u8>> = Vec::new();
    for line in contents.lines() {
        let mut vec: Vec<u8> = Vec::new();
        for token in line.split_ascii_whitespace() {
            vec.push(token.parse().unwrap());
        }
        parsed_contents.push(vec);
    }
    return parsed_contents;
}

fn main() {
    let filename = "../text-files/p018_triangle_num_sum.txt";

    let parsed_contents = parse_file_contents(filename);

    println!("{:?}", parsed_contents);
}
