package main

import (
	"fmt"
	"os"
	"strconv"
	s "strings"
)

func isDebug() bool {
	return true
}

func contain[T comparable](list []T, x T) bool {
	for _, v := range list {
		if v == x {
			return true
		}
	}
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
//	part2()
}

func part1() {
	ret := 0
	input := getInput()
	for _, val := range input {
		fmt.Println(val)
	}

	fmt.Println("Part 1:", ret)
}

func part2() {
	ret := 0
	input := getInput()
	for _, val := range input {
		fmt.Println(val)
	}

	fmt.Println("Part 2:", ret)
}