/*
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
*/

fn main() {
    let base: u128 = 2;
    let mut total: i32 = 0;
    for i in 1..=64 {
        let solution: u128 = base.pow(i);
        let sol = solution.to_string();
        let last_total = total;
        total = 0;
        for digit in sol.chars() {
            total += digit.to_digit(10).unwrap() as i32;
        }
        let difference: i32 = total - last_total;
        //println!("{} + {} = {}", last_total, difference, total);
        println!("{}", difference);
    }
}
