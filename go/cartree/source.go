package main

import "fmt"

// https://en.wikipedia.org/wiki/Cartesian_tree
// Builds using the first linear-time method.

type Node struct {
	P *Node
	L *Node
	R *Node
	D  int
}


func Cons(d int, l *Node, r *Node) *Node {
	node := &Node{nil, nil, nil, d}
	node.SetL(l)
	node.SetR(r)
	return node
}

func (this *Node) SetL(l *Node) {
	this.L = l
	if l != nil {
		l.P = this
	}
}

func (this *Node) SetR(r *Node) {
	this.R = r
	if r != nil {
		r.P = this
	}
}

func (this *Node) Dump() {
	if this == nil {
		fmt.Print("-")
		return
	}

	if this.L == nil && this.R == nil {
		fmt.Printf("%d", this.D)
		return
	}

	fmt.Print("(")
	this.L.Dump()
	fmt.Printf(" %d ", this.D)
	this.R.Dump()
	fmt.Print(")")
}


func main() {
	var root *Node = nil
	var curr *Node = nil
	var data int

	for {
		n, err := fmt.Scan(&data)
		if n != 1 || err != nil {
			break
		}

		for curr != nil && curr.D > data {
			curr = curr.P
		}

		if curr == nil {
			curr = Cons(data, root, nil)
			root = curr
		} else {
			tmp := Cons(data, curr.R, nil)
			curr.SetR(tmp)
			curr = tmp
		}
	}

	root.Dump()
	fmt.Println()
}
