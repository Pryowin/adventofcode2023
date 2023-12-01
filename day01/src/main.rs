use day01;
use std::env::args;

const DIGITS: [&str; 10] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const DIGITS_AS_TEXT: [&str; 10] = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];
fn main() {
    let args: Vec<String> = args().collect();

    let input = day01::read_file(args[2].as_str());

    let mut sum = 0;
    for line in input {
        if args[1] == "A".to_string() {
            sum += calibration_value(line)
        } else {
            sum += calibration_value_b(line)
        }
    }

    println!("Calibration total is {}", sum);
}

fn calibration_value(line: String) -> usize {
    let mut is_first_digit_found = false;
    let mut value: usize = 0;
    let mut last_digit: usize = 0;

    for chr in line.chars() {
        if !is_first_digit_found {
            if chr.is_digit(10) {
                is_first_digit_found = true;
                last_digit = chr.to_digit(10).unwrap() as usize;
                value = 10 * last_digit;
            }
        } else {
            if chr.is_digit(10) {
                last_digit = chr.to_digit(10).unwrap() as usize;
            }
        }
    }
    value += last_digit;
    value
}
fn calibration_value_b(line: String) -> usize {
    let mut first_digit: usize = 0;
    let mut last_digit: usize = 0;
    let mut first_location: usize = line.len();
    let mut last_location: usize = 0;

    for i in 0..=9 {
        let result = line.find(DIGITS[i]);
        match result {
            Some(x) => {
                /* println!(
                    "1st loc {}, first digit {}, last loc {}, last_digit {}, x={}, i={}",
                    first_location, first_digit, last_location, last_digit, x, i
                ); */
                if x < first_location {
                    first_location = x;
                    first_digit = i;
                }
                if x >= last_location {
                    last_location = x;
                    last_digit = i;
                }
            }
            _ => (),
        }
        let result = line.rfind(DIGITS[i]);
        match result {
            Some(x) => {
                /* println!(
                    "1st loc {}, first digit {}, last loc {}, last_digit {}, x={}, i={}",
                    first_location, first_digit, last_location, last_digit, x, i
                ); */
                if x < first_location {
                    first_location = x;
                    first_digit = i;
                }
                if x >= last_location {
                    last_location = x;
                    last_digit = i;
                }
            }
            _ => (),
        }
    }
    for i in 0..=9 {
        let result = line.find(DIGITS_AS_TEXT[i]);
        match result {
            Some(x) => {
                if x < first_location {
                    first_location = x;
                    first_digit = i;
                }
                if x >= last_location {
                    last_location = x;
                    last_digit = i;
                }
            }
            _ => (),
        }
        let result = line.rfind(DIGITS_AS_TEXT[i]);
        match result {
            Some(x) => {
                if x < first_location {
                    first_location = x;
                    first_digit = i;
                }
                if x >= last_location {
                    last_location = x;
                    last_digit = i;
                }
            }
            _ => (),
        }
    }
    // println!("{} : {} & {}", line, first_digit, last_digit);
    let value = first_digit * 10 + last_digit;
    value
}
