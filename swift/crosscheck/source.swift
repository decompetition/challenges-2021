import Foundation

var wpath = "/usr/share/dict/words"
var lines: [String] = []

switch CommandLine.arguments.count {
  case 2:
    wpath = CommandLine.arguments[1]
  case 1:
    break
  default:
    print("USAGE: ./crosscheck [words-file]")
    exit(1)
}

// Load valid words...
guard let data = try? String(contentsOfFile: wpath, encoding: .utf8) else {
  print("Could not open words file.")
  exit(1)
}

let words = Set(data.components(separatedBy: .newlines))

// Read user input...
while let line = readLine() {
  lines.append(line)
}

// Make sure it's not empty...
guard let maxlen = lines.map({$0.count}).max() else {
  exit(0) // But it's okay if it is!
}

// Validate horizontally...
var errors: [String] = []
for line in lines {
  var word = ""
  for char in line {
    if char.isWhitespace {
      if word.count > 1 && !words.contains(word) {
        errors.append(word)
      }

      word = ""
    }
    else {
      word.append(char)
    }
  }

  if word.count > 1 && !words.contains(word) {
    errors.append(word)
  }
}

// Validate vertically...
for i in 0 ..< maxlen {
  var word = ""
  for line in lines {
    let index = line.index(line.startIndex, offsetBy: i, limitedBy: line.endIndex)
    if index == nil || index! >= line.endIndex || line[index!].isWhitespace {
      if word.count > 1 && !words.contains(word) {
        errors.append(word)
      }

      word = ""
    }
    else {
      word.append(line[index!])
    }
  }

  if word.count > 1 && !words.contains(word) {
    errors.append(word)
  }
}

// Success!
if errors.count == 0 {
  exit(0)
}

// Failure...
print("Invalid words:")
for word in errors {
  print(" - " + word)
}

exit(1)
