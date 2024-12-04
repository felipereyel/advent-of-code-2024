package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func mustAtoi(s string) int {
	r, err := strconv.Atoi(s)

	if err != nil {
		panic("bad atoi input")
	}

	return r
}

func mul(s string) int {
	total := 0
	expr := regexp.MustCompile("mul\\((\\d{1,3},\\d{1,3})\\)")
	for _, match := range expr.FindAllStringSubmatch(s, -1) {
		parts := strings.Split(match[1], ",")
		total += mustAtoi(parts[0]) * mustAtoi(parts[1])
	}

	return total
}

func main() {
	file := os.Args[1]

	bcontent, err := os.ReadFile(file)
	if err != nil {
		panic("Failed to open file")
	}

	scontent := string(bcontent)

	total := 0
	for _, segment := range strings.Split(scontent, "do()") {
		parts := strings.Split(segment, "don't()")
		total += mul(parts[0])
	}

	fmt.Println(total)
}
