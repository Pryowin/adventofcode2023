use day02;
use std::cmp;
use std::env::args;

const RED: u32 = 12;
const GREEN: u32 = 13;
const BLUE: u32 = 14;
const END_OF_GAME_NUMBER_MARKER: char = ':';
const GRAB_DELIM: char = ';';
const COLOR_DELIM: char = ',';

struct Balls {
    red: u32,
    blue: u32,
    green: u32,
}
impl Balls {
    fn total(self) -> u32 {
        self.red + self.blue + self.green
    }

    fn is_possible(self, compare: &Balls) -> bool {
        let red = self.red;
        let green = self.green;
        let blue = self.blue;
        let total = self.total();

        if red > compare.red || blue > compare.blue || green > compare.green {
            return false;
        }
        return total <= 39;
    }
}

fn main() {
    let args: Vec<String> = args().collect();
    let run_type = &args[1];
    let input = day02::read_file(args[2].as_str());

    if run_type == "A" {
        println!("Answer is {}", part_one(input));
    } else {
        println!("Answer is {}", part_two(input));
    }
}
fn part_one(input: Vec<String>) -> u32 {
    let mut answer = 0;
    let elf_question = Balls {
        red: RED,
        blue: BLUE,
        green: GREEN,
    };

    for line in input {
        let game = get_game(&line);
        if is_game_possible(&line, &elf_question) {
            answer += game;
        }
    }
    answer
}
fn part_two(input: Vec<String>) -> u32 {
    let mut answer = 0;
    for line in input {
        let balls = get_max(&line);
        answer += balls.red * balls.blue * balls.green;
    }
    answer
}
fn get_max(line: &str) -> Balls {
    let mut max_balls = Balls {
        red: 0,
        blue: 0,
        green: 0,
    };

    let balls = get_balls(&line);

    for grab in balls {
        max_balls.red = cmp::max(max_balls.red, grab.red);
        max_balls.green = cmp::max(max_balls.green, grab.green);
        max_balls.blue = cmp::max(max_balls.blue, grab.blue);
    }
    max_balls
}

fn is_game_possible(line: &str, elf_question: &Balls) -> bool {
    let game = get_balls(line);

    for grabs in game {
        if !grabs.is_possible(elf_question) {
            return false;
        }
    }
    true
}
fn get_game(line: &str) -> u32 {
    let mut build_number: String = String::new();
    for chr in line[5..].chars() {
        if chr == END_OF_GAME_NUMBER_MARKER {
            break;
        } else {
            build_number.push(chr);
        }
    }

    let return_result: u32 = match build_number.trim().parse() {
        Ok(num) => num,
        Err(_) => 0,
    };
    return_result
}
fn get_balls(line: &str) -> Vec<Balls> {
    let mut balls: Vec<Balls> = Vec::new();

    let start_pos = line.find(END_OF_GAME_NUMBER_MARKER).unwrap();

    for grab in line[start_pos + 1..].split(GRAB_DELIM) {
        let trimmed_grab = grab.trim();

        let ball_grab = Balls {
            red: get_count("red", &trimmed_grab),
            blue: get_count("blue", &trimmed_grab),
            green: get_count("green", &trimmed_grab),
        };
        balls.push(ball_grab);
    }

    return balls;
}
fn get_count(color: &str, result: &str) -> u32 {
    let mut color_cnt_string: &str = "";
    for color_count in result.split(COLOR_DELIM) {
        let found = match color_count.find(color) {
            Some(_) => {
                color_cnt_string = color_count;
                true
            }
            None => false,
        };
        if found {
            break;
        }
    }
    if color_cnt_string == "" {
        return 0;
    }
    let mut count_string: String = String::new();
    for chr in color_cnt_string.trim().chars() {
        if chr == ' ' {
            break;
        } else {
            count_string.push(chr);
        }
    }

    let return_result: u32 = match count_string.trim().parse() {
        Ok(num) => num,
        Err(_) => 0,
    };
    return_result
}
