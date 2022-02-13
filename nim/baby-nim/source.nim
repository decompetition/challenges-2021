import os

if paramCount() != 1:
  echo "USAGE: ./greet name"
  system.quit(1)

let name = paramStr(1)
echo "Hello, ", name, "!"
