/*
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
*/
use std::vec;

fn power_two_vec(vec: &mut Vec<u8>)  {
    let i = 0;
    for num in vec{
        vec[i] = *num * 2;
    }
    
}


/*
fn old_main() {
    let base: u128 = 2;
    let mut total: i32 = 0;
    for i in 1..=127 {
        let solution: u128 = base.pow(i);
        let sol = solution.to_string();
        let last_total = total;
        total = 0;
        for digit in sol.chars() {
            total += digit.to_digit(10).unwrap() as i32;
        }
        let difference: i32 = total - last_total;
        println!("2^{} = {}", i, solution);
        println!("       Sum: {}", total);
        println!("       Delta: {}\n", difference);
        //println!("{}", difference);
        vector
    }
}
*/


fn main() {
    let mut v: Vec<u8> = vec!(1);
    println!("{:?}", v);
    power_two_vec(&mut v);
    println!("{:?}", v);
}
