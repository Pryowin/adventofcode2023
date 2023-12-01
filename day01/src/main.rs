use day01;
use std::env::args;

fn main() {
    let args: Vec<String> = args().collect();

    let input = day01::read_file(args[2].as_str());

    let mut sum = 0;
    if args[1] == "A".to_string() {
        for line in input {
            sum += calibration_value(line)
        }
    } else {
    }

    println!("Calibration total is {}", sum);
}

fn calibration_value(line: String) -> u32 {
    let mut is_first_digit_found = false;
    let mut value = 0;
    let mut last_digit = 0;

    for chr in line.chars() {
        if !is_first_digit_found {
            if chr.is_digit(10) {
                is_first_digit_found = true;
                last_digit = chr.to_digit(10).unwrap();
                value = 10 * last_digit;
            }
        } else {
            if chr.is_digit(10) {
                last_digit = chr.to_digit(10).unwrap();
            }
        }
    }
    value += last_digit;
    value
}
