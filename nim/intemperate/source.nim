import os
import strformat
import strutils
import tables

var map = {
  "K": (1.0,   0.00),
  "F": (1.8, 459.67),
  "C": (1.0, 273.15)
}.toTable()

if paramCount() != 2:
  echo "USAGE: ./convert value unit"
  system.quit(1)

try:
  let value  = parseFloat(paramStr(1))
  let args   = map[paramStr(2)]
  let kelvin = (value + args[1]) / args[0]

  for u, pair in map.pairs:
    let val = kelvin * pair[0] - pair[1]
    echo fmt"= {val:>7.2f} {u}"

except KeyError:
  echo "Unknown unit."
  system.quit(212)
except ValueError:
  echo "Invalid number."
  system.quit(32)
