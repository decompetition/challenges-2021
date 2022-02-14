# Decompetition 2021 Challenges

This is the full set of challenges used for Decompetition v2.0, also known as
Decompetition 2021 (it technically ran in 2022, but we figure that sequential
version numbers are more important than mere facts).

Challenges are grouped by language.  Inside each challenge folder you'll find:

- `binary.out` is the binary itself.  Debug symbols are removed.
- `deco.py` is a symlink to the test helper.  The real file is in the root of the repo.
- `disasm.yml` contains disassembly for all the functions we care about.
- `source.xxx` is the original source code for the binary.
- `starter.xxx` is the starting source code that was provided to the players.
- `test.py` contains the secret test cases that were used to check functionality.


## The C Challenges

### `baby-c`

This is a simple Title Casing program.  It reads `char`s from standard input and
writes the title-cased versions to standard output: letters following spaces or
at the beginning of strings are capitalized, and everything else is lower case.

### `daedalus`

The architect.  Builds mazes using a custom [disjoint set](https://en.wikipedia.org/wiki/Disjoint_sets)
data structure and [Kruskal's Algorithm](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm),
then prints it to the console.

### `demesne`

Generates pseudo-random `.biz` domain names, in the spirit of a botnet looking
for its next command and control server.  It takes a random seed as a command
line argument, then generates sixteen domain names.

### `dublin`

A sorted, doubly-linked list using [XOR pointer compression](https://en.wikipedia.org/wiki/XOR_linked_list).
It reads a list of integers from standard input, and then prints them in both
ascending and descending order.

### `leipzig`

A horribly hacky [Hailstone Sequence](https://en.wikipedia.org/wiki/Collatz_conjecture)
calculator, implemented entirely with signal handlers and long jumps.  Watch out
for the `volatile` PID variable!

### `malware`

Fake malware.  It hides its process name, aborts in the presence of standard
analysis tools, and downloads and runs scripts from a command and control
server (actually just localhost).

### `rotterdam`

A ROT-N encryptor and decryptor, implemented without using the C standard
library.  Instead, it talks directly to the OS through the functions in the
`unistd.h` header.

### `winkey`

Please type your 20-digit Product Identification Number, which is located on
your Certificate of Authenticity.  This program will make sure it's a valid
Windows 95 activation key.


## The C++ Challenges

### `baby-cpp`

A [perfect number](https://en.wikipedia.org/wiki/Perfect_number) detector.  Only
accepts perfect numbers.  Other numbers are judged unworthy and rejected.

### `blaise`

Generates rows from [Pascal's Triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle).
When given one command line argument, it'll print rows from row zero up until
that row.  When given two, it'll print from the first to the second.  All ranges
are inclusive.

### `rumrum`

A brute-force [MurmurHash](https://en.wikipedia.org/wiki/MurmurHash) cracker.
It takes a charset, a length, and a target hash value from the command line,
then spawns a producer thread that generates possible passwords and a worker
thread that hashes them and sees if there's a match.  It uses the "one at a
time" version of MurmurHash described [here](https://stackoverflow.com/a/57960443).

### `yurlungur`

The `cat` of many colors.  It adds [ANSII escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code#Colors)
to colorize its standard input before printing it to standard output.  To keep
the color transitions smooth, it uses the C++ random module to perform a random
walk in a 6x6x6 RGB color cube.  It's named after the Australian Aboriginal
[Rainbow Serpent](https://en.wikipedia.org/wiki/Rainbow_Serpent).


## The Go Challenges

### `baby-go`

A DrUnKeNCAsInG utility.  Reads from standard input and flips the capitalization
of every other character.

### `cartree`

Reads numbers form standard input and assembles them into a [Cartesian
Tree](https://en.wikipedia.org/wiki/Cartesian_tree), then prints the resulting
structure.

### `goalie`

Animated command-line [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life).
It uses more [ANSII escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_%40Control_Sequence_Introducer%41_sequences)
to reset the cursor position and overdraw the board each frame.  The board is
toroidal, and "wraps" at the edges; this is implemented with a step that copies
the edges of the board around before evaluating the next generation.

### `oracle`

Console [Magic 8-Ball](https://en.wikipedia.org/wiki/Magic_8-ball).  Collects
personally identifying information from the user, then uses it to seed a random
number generator and select a fortune.  Next year we'll be collecting credit
card numbers as well.

### `scaffold`

[Hangman](https://en.wikipedia.org/wiki/Hangman_%40game%41), but without the
cutting-edge graphics.


## The Nim Challenges

### `baby-nim`

Takes a name as a command line argument, then prints a greeting for that user.
Somehow, this produces over three hundred lines of assembly.

### `intemperate`

Takes a number and a (temperature) unit as command line arguments, then prints
it converted to all the units it knows about.  Understands
[Kelvin](https://en.wikipedia.org/wiki/Kelvin),
[Fahrenheit]https://en.wikipedia.org/wiki/Fahrenheit, and
[Celsius](https://en.wikipedia.org/wiki/Celsius).
This was originally going to be the `baby-nim` challenge.  Then I saw the
assembly code...


## The Rust Challenges

### `baby-rust`

Takes a single command line argument, uses a recursive function to reverse the
string, and prints the result.

### `braintrust`

A [Brainfuck](https://en.wikipedia.org/wiki/Brainfuck) interpreter - essentially
a [Turing Machine](https://en.wikipedia.org/wiki/Turing_machine).  It uses a
pair of stacks to store the "tape" on either side of the current cell.

### `endeavour`

A [Morse Code](https://en.wikipedia.org/wiki/Morse_code) encoder and decoder.
It uses a list of letters stored in a [compact binary heap](https://en.wikipedia.org/wiki/Ahnentafel).

### `parasite`

A [SKATS](https://en.wikipedia.org/wiki/SKATS) encoder and decoder.  It
translates [Hangul script](https://en.wikipedia.org/wiki/Hangul) to an encoding
in [Latin script](https://en.wikipedia.org/wiki/Latin_script) or vice versa.
It can be used alongside `endeavour` to get a full Korean-to-Morse translation
like in [the movie](https://en.wikipedia.org/wiki/Parasite_%402019_film%41).


## The Swift Challenges

### `baby-swift`

Calculates the [Lanczos approximation](https://en.wikipedia.org/wiki/Lanczos_approximation)
of the [Gamma function](https://en.wikipedia.org/wiki/Gamma_function).  Loops
over numbers read from standard input.

### `crosscheck`

Reads a [crossword puzzle](https://en.wikipedia.org/wiki/Crossword) from
standard input, and makes sure that all the words in the puzzle are contained
in a user-specified words file.

### `diffcult`

A [unified diff format](https://en.wikipedia.org/wiki/Diff#Unified_format)
colorizer.  Reads a diff from standard input and adds
[ANSI escape codes](https://en.wikipedia.org/wiki/ANSI_escape_code#SGR_%40Select_Graphic_Rendition%41_parameters)
to make it easier to read.
