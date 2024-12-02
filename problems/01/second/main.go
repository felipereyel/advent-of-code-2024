package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

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
	freqs := make(map[int]int)

	for i, line := range lines {
		parts := strings.Split(line, "   ")

		lefts[i], err = strconv.Atoi(parts[0])
		if err != nil {
			panic("bad left value")
		}
		right, err := strconv.Atoi(parts[1])
		if err != nil {
			panic("bad right value")
		}

		freqs[right] += 1
	}

	total := 0
	for _, left := range lefts {
		total += left * freqs[left]
	}

	fmt.Println(total)
}
