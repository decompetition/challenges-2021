use std::char;
use std::io;

use std::collections::HashMap;
use std::iter::Peekable;

// Encodes and decodes SKATS Hangul.
// https://en.wikipedia.org/wiki/SKATS
// https://en.wikipedia.org/wiki/Korean_language_and_computers#Hangul_Syllables_block

// Codes for Initial, Medial, and Final jamo.
const I: &'static str = "L?LL?F?B?BB?V?M?W?WW?G?GG?K?P?PP?C?X?Z?O?J";
const M: &'static str = "E?EU?I?IU?T?TU?S?SU?A?AE?AEU?AU?N?H?HT?HTU?HU?R?D?DU?U";
const F: &'static str = "?L?LL?LG?F?FP?FJ?B?V?VL?VM?VW?VG?VZ?VO?VJ?M?W?WG?G?GG?K?P?C?X?Z?O?J";

fn enco(input: &str) -> String {
  let imap: Vec<&str> = I.split("?").collect();
  let mmap: Vec<&str> = M.split("?").collect();
  let fmap: Vec<&str> = F.split("?").collect();

  let mut result = String::new();
  for c in input.chars() {
    if c >= '가' && c <= '힣' {
      let n = (c as usize) - 44032;

      //  I * 588 + M  * 28 + F
      // (I *  21 + M) * 28 + F

      result += imap[n / 588];
      result += mmap[n % 588 / 28];
      result += fmap[n % 28];
      result += " ";
    }
    else if c == ' ' {
      result += " ";
    }
  }

  result.truncate(result.trim_end().len());
  return result;
}

fn read(map: &HashMap<&str, usize>, iter: &mut Peekable<impl Iterator<Item=char>>) -> Option<usize> {
  let mut val: Option<usize> = None;
  let mut key = String::new();

  loop {
    match iter.peek() {
      None => return val,
      Some(c) => {
        key.push(*c);
        match map.get(&*key) {
          None => return val,
          Some(v) => {
            val = Some(*v);
            iter.next();
          }
        }
      }
    }
  }
}

fn deco(input: &str) -> String {
  let imap: HashMap<&str, usize> = I.split("?").enumerate().map(|(i, v)| (v, i)).collect();
  let mmap: HashMap<&str, usize> = M.split("?").enumerate().map(|(i, v)| (v, i)).collect();
  let fmap: HashMap<&str, usize> = F.split("?").enumerate().map(|(i, v)| (v, i)).collect();

  let mut result = String::new();
  let uppercase  = input.to_ascii_uppercase();
  let mut iter   = uppercase.chars().peekable();

  while iter.peek().is_some() {
    let ti = read(&imap, iter.by_ref());
    let tm = read(&mmap, iter.by_ref());
    let tf = read(&fmap, iter.by_ref());

    match (ti, tm) {
      (Some(xi), Some(xm)) => {
        let n = 588 * xi + 28 * xm + tf.unwrap_or(0) + 44032;
        let c = std::char::from_u32(n as u32);
        result.push(c.unwrap());
      }
      _ => {}
    }

    let _ = iter.by_ref().take_while(|c| *c != ' ');
    iter.next();

    if iter.peek() == Some(&' ') {
      result.push(' ');
      iter.next();
    }
  }

  return result;
}

fn main() {
  let arg  = std::env::args().nth(1).unwrap_or("nope".to_string());
  let func = match arg.as_str() {
    "-e" => enco,
    "-d" => deco,
    _    => {
      println!("USAGE: ./parasite -[de]");
      return
    }
  };

  loop {
    let mut input = String::new();
    match io::stdin().read_line(&mut input) {
      Ok(0)  => break,
      Err(_) => break,
      Ok(_)  => {
        println!("{}", func(input.trim_end()))
      }
    }
  }
}
