package main

import (
    "flag"
    "fmt"
    "math/rand"
    "os"
    "os/signal"
    "syscall"
    "time"
)

var OFFSETS = [][]int {
    []int {-1, -1},
    []int {-1,  0},
    []int {-1, +1},
    []int { 0, +1},
    []int {+1, +1},
    []int {+1,  0},
    []int {+1, -1},
    []int { 0, -1}}

type Field struct {
    W uint
    H uint

    data [][]bool
    temp [][]bool
}

func (this *Field) Draw() {
    for y := uint(1); y < this.H; y++ {
        for x := uint(1); x < this.W; x++ {
            if this.data[y][x] {
                fmt.Print("*")
            } else {
                fmt.Print(" ")
            }
        }

        fmt.Println()
    }
}

func (this *Field) Seed() {
    for y := uint(1); y < this.H; y++ {
        for x := uint(1); x < this.W; x++ {
            this.data[y][x] = rand.Intn(2) == 0
        }
    }
}

func (this *Field) Step() {
    this.Wrap()
    w := int(this.W)
    h := int(this.H)

    for y := 1; y < h; y++ {
        for x := 1; x < w; x++ {
            count := 0

            for _, d := range OFFSETS {
                if this.data[y + d[0]][x + d[1]] {
                    count += 1
                }
            }

            if this.data[y][x] {
                this.temp[y][x] = 2 <= count && count <= 3
            } else {
                this.temp[y][x] = count == 3
            }
        }
    }

    this.data, this.temp = this.temp, this.data
}

func (this *Field) Wrap() {
    h := this.H
    g := h - 1

    w := this.W
    v := w - 1

    for x := uint(1); x < w; x++ {
        this.data[0][x] = this.data[g][x]
        this.data[h][x] = this.data[1][x]
    }

    for y := uint(0); y <= h; y++ {
        this.data[y][0] = this.data[y][v]
        this.data[y][w] = this.data[y][1]
    }
}


func NewArray(w uint, h uint) [][]bool {
    data := make([][]bool, h)
    for i := uint(0); i < h; i++ {
        data[i] = make([]bool, w)
    }

    return data
}

func NewField(w uint, h uint) *Field {
    return &Field{w, h, NewArray(w+1, h+1), NewArray(w+1, h+1)}
}


func main() {
    os.Args[0] = "goalie"
    f := flag.Duration("f", 314 * time.Millisecond, "frame delay")
    w := flag.Uint(    "w",                     40, "width")
    h := flag.Uint(    "h",                     20, "height")
    n := flag.Uint(    "n",                      0, "frames")
    q := flag.Bool(    "q",                  false, "quiet")
    s := flag.Int64(   "s",                      0, "seed")
    flag.Parse()

    if *s == 0 {
        rand.Seed(time.Now().UnixNano())
    } else {
        rand.Seed(*s)
    }

    go func() {
        sigchan := make(chan os.Signal, 1)
        signal.Notify(sigchan, syscall.SIGTERM, syscall.SIGINT)
        <-sigchan
        *n = 1
    }()

    board := NewField(*w, *h)
    board.Seed()

    for i := uint(0); *n == 0 || i < *n; i++ {
        board.Step()

        if !*q {
            if i != 0 {
                fmt.Printf("\033[%dF", board.H - 1)
            }

            board.Draw()
            time.Sleep(*f)
        }
    }

    if *q {
        board.Draw()
    }
}
