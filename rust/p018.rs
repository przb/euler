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
const MAIN_ARRAY_LENGTH: usize = 15;

fn parse_file_contents(filename: &str) -> Vec<Vec<u32>> {
    let contents = fs::read_to_string(filename).expect("Something went wrong reading the file");

    let mut parsed_contents: Vec<Vec<u32>> = Vec::new();
    for line in contents.lines() {
        let mut vec: Vec<u32> = Vec::new();
        for token in line.split_ascii_whitespace() {
            vec.push(token.parse().unwrap());
        }
        parsed_contents.push(vec);
    }
    return parsed_contents;
}

fn find_path(contents: &Vec<Vec<u32>>) -> [usize; MAIN_ARRAY_LENGTH] {
    let mut indexes: [usize; MAIN_ARRAY_LENGTH] = [0; MAIN_ARRAY_LENGTH];

    let sum = contents[0][0];
    let mut i = 0;
    for row_index in 1..contents.len() {
        let sum_one = contents[row_index][i] + sum;
        let sum_two = contents[row_index][i + 1] + sum;
        if sum_one < sum_two{
            i += 1;
        }
        indexes[row_index] = i;
    }
    return indexes;
}

fn find_total(contents: &Vec<Vec<u32>>, path: [usize;MAIN_ARRAY_LENGTH]) -> u32{
    let mut total = 0;
    let mut i: usize = 0;
    for index in path{
        total += contents[i][index];
        i += 1;
    }
    return total;
}

// Current Algorithm
/**
 * for each number in the current row
 *      find the sum of both of the options in the next row
 * use the biggest sum
 */

fn main() {
    let filename = "../text-files/p018_triangle_num_sum.txt";

    let parsed_contents = parse_file_contents(filename);

    let path = find_path(&parsed_contents);

    let total = find_total(&parsed_contents, path);

    println!("{}", total)
    // println!("{:?}", parsed_contents);
}
