use std::env;
use std::io;

// Encoder and decoder for the Morse alphabet.
// https://en.wikipedia.org/wiki/Morse_code

const SHRDLU: &'static str = "?ETIANMSURWDKGOHVF?L?PJBXCYZQ??";

fn enco(key: &Vec<char>, input: &str) -> String {
  let mut result = String::new();
  let mut broken = false;

  for c in input.to_ascii_uppercase().chars() {
    if c == ' ' {
      result.push('/');
      broken = false;
      continue;
    }

    if broken {
      result.push(' ');
      broken = false;
    }

    if c == '?' {
      result.push('?');
      continue;
    }

    match key.iter().position(|&x| x == c) {
      None    => result.push('?'),
      Some(x) => {
        let mut i = x;
        let mut v: Vec<char> = vec!();
        broken = true;

        while i > 0 {
          if i & 1 == 1 {
            v.push('.');
          }
          else {
            v.push('-');
          }

          i = (i - 1) / 2;
        }

        for c in v.iter().rev() {
          result.push(*c);
        }
      }
    }
  }

  return result;
}

fn deco(key: &Vec<char>, input: &str) -> String {
  let mut result = String::new();
  let mut index  = 0;

  for c in input.chars() {
    if c == '.' {
      index += 1;
      index *= 2;
      index -= 1;
    }
    else if c == '-' {
      index += 1;
      index *= 2;
    }
    else if c == ' ' || c == '/' {
      if index > 0 {
        result.push(*key.get(index).unwrap_or(&'?'));
        index = 0;
      }

      if c == '/' {
        result.push(' ');
      }
    }
    else {
      result.push('?');
      index = 0;
    }
  }

  if index > 0 {
    result.push(*key.get(index).unwrap_or(&'?'));
  }

  return result;
}

fn trim(s: &mut String) {
  if s.ends_with('\n') {
    s.pop();
    if s.ends_with('\r') {
      s.pop();
    }
  }
}

fn main() {
  let key:  Vec<char> = SHRDLU.chars().collect();
  let args: Vec<String> = env::args().collect();

  if args.len() != 2 {
    println!("USAGE: ./endeavour -[de]");
    return
  }

  let func = if args[1] == "-e" {
    enco
  }
  else if args[1] == "-d" {
    deco
  }
  else {
    println!("USAGE: ./endeavour -[de]");
    return
  };

  loop {
    let mut input = String::new();
    match io::stdin().read_line(&mut input) {
      Ok(0)  => break,
      Err(_) => break,
      Ok(_)  => {
        trim(&mut input);
        println!("{}", func(&key, &input))
      }
    }
  }
}
