import Foundation

// Lanczos apprximation of the gamma function.
// https://en.wikipedia.org/wiki/Lanczos_approximation

let A: [Double] = [
    676.5203681218851,
  -1259.1392167224028,
    771.32342877765313,
   -176.61502916214059,
     12.507343278686905,
     -0.13857109526572012,
      0.0000099843695780195716,
      0.00000015056327351493116
]

func meet(_ arg: Double) -> Double {
  var z = arg

  if z < 0.5 {
    return Double.pi / (sin(Double.pi * z) * meet(1 - z))
  }
  else {
    z -= 1
    var x = 0.99999999999980993
    for (i, pval) in A.enumerated() {
      x += pval / (z + Double(i) + 1)
    }

    let t = z + Double(A.count) - 0.5
    return sqrt(2 * Double.pi) * pow(t, z + 0.5) * exp(-t) * x
  }
}

print("Γ ", terminator: "")
while let line = readLine() {
  if let z = Double(line) {
    print(String(format: "= %.6f", meet(z)))
  }
  else {
    print("Invalid.")
  }

  print("Γ ", terminator: "")
}
