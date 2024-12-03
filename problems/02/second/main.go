package main

import (
	"fmt"
	"math"
	"os"
	"slices"
	"strconv"
	"strings"
)

func atoiArray(s []string) ([]int, error) {
	out := make([]int, len(s))
	var err error

	for idx, v := range s {
		out[idx], err = strconv.Atoi(v)
		if err != nil {
			return nil, err
		}
	}

	return out, nil
}

func isSafe(iparts []int) bool {
	currDir := 0
	for i := range len(iparts) - 1 {
		dir := iparts[i] - iparts[i+1]

		absdir := math.Abs(float64(dir))
		if absdir <= 0 || absdir > 3 {
			return false
		}

		if currDir == 0 {
			currDir = dir
			continue
		}

		changes := dir * currDir
		if changes < 0 {
			return false
		}
	}

	return true
}

func main() {
	file := os.Args[1]

	bcontent, err := os.ReadFile(file)
	if err != nil {
		panic("Failed to open file")
	}

	scontent := string(bcontent)

	lines := strings.Split(scontent, "\n")
	safe := 0
	for _, line := range lines {
		sparts := strings.Fields(line)
		iparts, err := atoiArray(sparts)
		if err != nil {
			panic("bad parts")
		}

		if isSafe(iparts) {
			safe += 1
			continue
		}

		for i := range len(iparts) {
			subparts := slices.Concat(iparts[:i], iparts[i+1:])
			if isSafe(subparts) {
				safe += 1
				break
			}
		}
	}

	fmt.Println(safe)
}
