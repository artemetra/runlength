use runlength::*;

use std::env;

fn main() {
    let args_vec: Vec<_> = env::args().collect();
    let arg = args_vec.get(1).unwrap();
    let encoded = RunLengthEncoded::encode(&arg);
    println!("{}", encoded)
}
