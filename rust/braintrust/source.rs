use std::env;
use std::io::Read;
use std::io::Write;
use std::collections::HashMap;

struct State {
  jt: HashMap<usize, usize>,
  tl: Vec<u8>,
  tr: Vec<u8>,
  tc: u8
}

impl State {
  fn new(code: &[u8]) -> State {
    let mut s: Vec<usize> = Vec::new();
    let mut m: HashMap<usize, usize> = HashMap::new();
    for (i, c) in code.iter().enumerate() {
      if *c == 91 {s.push(i);}
      if *c == 93 {
        let j = s.pop().unwrap();
        m.insert(i, j);
        m.insert(j, i);
      }
    }

    assert!(s.len() == 0);
    State {
      jt: m,
      tl: Vec::new(),
      tr: Vec::new(),
      tc: 0
    }
  }

  fn diff(&mut self, delta: i8) {
    self.tc = self.tc.wrapping_add(delta as u8);
  }

  fn dump(&self) {
    let buffer = [self.tc];
    std::io::stdout().write(&buffer).ok();
  }

  fn step(&mut self, fwd: bool) {
    if fwd {
      self.tl.push(self.tc);
      self.tc = self.tr.pop().unwrap_or(0);
    }
    else {
      self.tr.push(self.tc);
      self.tc = self.tl.pop().unwrap_or(0);
    }
  }

  fn read(&mut self) {
    let mut buffer = [0u8];
    std::io::stdin().read_exact(&mut buffer).ok();
    self.tc = buffer[0];
  }

  fn jump(&mut self, i: usize, fwd: bool) -> usize {
    if fwd ^ (self.tc != 0) {
      self.jt[&i]
    }
    else {
      i
    }
  }
}


fn main() {
  let     input = env::args().nth(1).unwrap();
  let     code  = input.as_bytes();
  let mut state = State::new(code);
  let mut i     = 0usize;

  while i < code.len() {
    match code[i] {
      43 => state.diff(1),
      44 => state.read(),
      45 => state.diff(-1),
      46 => state.dump(),
      60 => state.step(true),
      62 => state.step(false),
      91 => i = state.jump(i, true),
      93 => i = state.jump(i, false),
      _  => {}
    }

    i += 1;
  }

  // println!();
}
