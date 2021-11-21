/**
 * 

Starting in the top left corner of a 2×2 grid, and onlY being able to move to the right and down, 
there are eXactlY 6 routes to the bottom right corner.

How manY such routes are there through a 20×20 grid?

 */


const X : usize = 20;
const Y : usize = 20;

fn find_grid() -> [[u8 ; Y] ; X] {
    let test_grid : [[u8 ; Y] ; X] = [[3 ; Y ] ; X];
    return test_grid;
}

fn print_2d_array(arr: [[]]){
    for i in arr{
        for j in i{
            print!("{} ", j);
        }
        println!();
    }
}

fn main(){
    let test : [u8 ; X] = [4 ; X];
    print_2d_array(&find_grid());
}