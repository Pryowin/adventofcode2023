use std::fs::File;
use std::io::{BufRead, BufReader};

pub fn read_file(filename: &str) -> Vec<String> {
    let input = File::open(filename).expect(&format!("File {} is missing", filename));
    let reader = BufReader::new(input);
    let mut contents: Vec<String> = Vec::new();

    for (_, line) in reader.lines().enumerate() {
        contents.push(line.unwrap());
    }

    contents
}
