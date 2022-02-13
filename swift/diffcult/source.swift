import Foundation

func setup() -> [String: (Int, Int)] {
  return [
    "@": (22, 34),
    "+": ( 1, 32),
    "-": ( 1, 31)
  ]
}

let map = setup()
while let line = readLine() {
  if line == "" {
    print()
    continue
  }
  else if let style = map[line.substring(to: 1)] {
    print(String(format: "\u{1b}[%d;%dm", style.0, style.1) + line + "\u{1b}[0m")
  }
  else {
    print(line)
  }
}
