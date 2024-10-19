package main

import (
	"fmt"
	"os"
	"strconv"
	s "strings"
)

func isDebug() bool {
	return false
}

func getInput() []string {
	name := "./input.txt"
	if isDebug() {
		name = "./sample.txt"
	}
	dat, err := os.ReadFile(name)
	if err != nil {
		panic(err)
	}
	return s.Split(string(dat), "\n")
}

func getIntInput() []int {
	input := getInput()
	list := make([]int, len(input))
	for i, val := range input {
		a, err := strconv.Atoi(val)
		if err != nil {panic(err)}
		list[i] = a
	}
	return list
}

func main() {
	part1()
	part2()
}

func colapse(input string) string {
	var lst []string
	skip := false
	length := len(input)
	for {
		for i, _ := range input {
			if i+1 >= len(input) {break}
			if skip {
				skip = false
				continue
			}
			if s.ToLower(input[i:i+1]) != s.ToLower(input[i+1:i+2]) || input[i:i+1] == input[i+1:i+2] {
				lst = append(lst, input[i:i+1])
			} else {
				skip = true
			}
		}
		lst = append(lst, input[len(input)-1:])
		input = s.Join(lst, "")
		lst = nil
		if length == len(input) {break}
		length = len(input)
	}
	return input
}

func part1() {
	ret := 0
	input := getInput()[0]


	ret = len(colapse(input))
	fmt.Println("Part 1:", ret)
}

func part2() {
	ret := 0

	length := 9999999999
	for r := 'a'; r < 'z'; r++ {
		input := getInput()[0]
		letter := fmt.Sprintf("%c", r)
		input = s.Replace(input, letter, "", -1)
		input = s.Replace(input, s.ToUpper(letter), "", -1)
		i := colapse(input)
		if len(i) < length {
			length = len(i)
		}
	}

	ret = length
	fmt.Println("Part 2:", ret)
}