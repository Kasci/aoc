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

func part1() {
	ret := 0
	input := getIntInput()
	for _, val := range input {
		ret += val
	}

	fmt.Println("Part 1:", ret)
}

func part2() {
	ret := 0
	input := getIntInput()
	i := 0
	value := 0
	var freq []int
	for {
		value += input[i]
		found := false
		for _, val := range freq {
			if val == value {
				found = true
				break
			}
		}
		if found {
			ret = value
			break
		}
		freq = append(freq, value)
		i = (i+1)%len(input)
	}

	fmt.Println("Part 2:", ret)
}