package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

func dist(a, b int) int {
	if a > b {
		return a - b
	}
	return b - a
}

func main() {
	file := os.Args[1]

	bcontent, err := os.ReadFile(file)
	if err != nil {
		panic("Failed to open file")
	}

	scontent := string(bcontent)

	lines := strings.Split(scontent, "\n")
	nlines := len(lines)
	lefts := make([]int, nlines)
	rights := make([]int, nlines)

	for i, line := range lines {
		parts := strings.Split(line, "   ")

		lefts[i], err = strconv.Atoi(parts[0])
		if err != nil {
			panic("bad left value")
		}
		rights[i], err = strconv.Atoi(parts[1])
		if err != nil {
			panic("bad right value")
		}
	}

	slices.Sort(lefts)
	slices.Sort(rights)

	total := 0
	for i := range nlines {
		total += dist(lefts[i], rights[i])
	}

	fmt.Println(total)
}
