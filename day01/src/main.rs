use day01;
use std::env::args;

const DIGITS: [&str; 10] = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"];
const DIGITS_AS_TEXT: [&str; 10] = [
    "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

struct DigitsInString {
    first_digit: usize,
    last_digit: usize,
    first_location: usize,
    last_location: usize,
}

fn main() {
    let args: Vec<String> = args().collect();

    let input = day01::read_file(args[2].as_str());

    let mut sum = 0;
    for line in input {
        if args[1] == "A".to_string() {
            sum += calibration_value(line, false)
        } else {
            sum += calibration_value(line, true)
        }
    }

    println!("Calibration total is {}", sum);
}

fn calibration_value(line: String, part_b: bool) -> usize {
    let mut calibration = DigitsInString {
        first_digit: 0,
        last_digit: 0,
        first_location: line.len(),
        last_location: 0,
    };

    for i in 0..=9 {
        let result = line.find(DIGITS[i]);
        calibration = find_digit(calibration, result, i);

        let result = line.rfind(DIGITS[i]);
        calibration = find_digit(calibration, result, i);
    }
    if part_b {
        for i in 0..=9 {
            let result = line.find(DIGITS_AS_TEXT[i]);
            calibration = find_digit(calibration, result, i);

            let result = line.rfind(DIGITS_AS_TEXT[i]);
            calibration = find_digit(calibration, result, i);
        }
    }
    let value = calibration.first_digit * 10 + calibration.last_digit;
    value
}
fn find_digit(mut calibration: DigitsInString, result: Option<usize>, i: usize) -> DigitsInString {
    match result {
        Some(x) => {
            if x < calibration.first_location {
                calibration.first_location = x;
                calibration.first_digit = i;
            }
            if x >= calibration.last_location {
                calibration.last_location = x;
                calibration.last_digit = i;
            }
        }
        _ => (),
    }
    calibration
}
