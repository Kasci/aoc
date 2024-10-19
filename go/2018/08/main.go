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

func contain[T comparable](list []T, x T) bool {
	for _, v := range list {
		if v == x {
			return true
		}
	}
	return false
}

func apnd[T comparable](list []T, x T) []T {
	for _, v := range list {
		if v == x {
			return list
		}
	}
	return append(list, x)
}

func rmv[T comparable](list []T, x T) []T {
	var ret []T
	for _, v := range list {
		if v != x {
			ret = append(ret, v)
		}
	}
	return ret
}

func rmv2[T comparable](list [][]T, x T, f func([]T) T) [][]T {
	var ret [][]T
	for _, v := range list {
		if f(v) != x {
			ret = append(ret, v)
		}
	}
	return ret
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

func check(in []int) ([]int, int) {
	children := in[0]
	metadata := in[1]
	sum := 0
	n := 0
	in = in[2:]
	if children > 0 {
		for range children {
			in, n = check(in)
			sum += n
		}
	}
	for i := range metadata {
		sum += in[i]
	}
	return in[metadata:], sum
}

func check2(in []int) ([]int, int) {
	children := in[0]
	metadata := in[1]
	var sum []int
	value := 0
	n := 0
	in = in[2:]
	if children > 0 {
		for range children {
			in, n = check2(in)
			sum = append(sum, n)
		}
	}
	for i := range metadata {
		if children > 0 {
			k := in[i]-1
			if k < len(sum) {
				value += sum[k]
			}
		} else {
			value += in[i]
		}
	}
//	fmt.Println(children, metadata, sum, in[:metadata], value)
	return in[metadata:], value
}

func main() {
	part1()
	part2()
}

func part1() {
	ret := 0
	input := getInput()[0]
	var in []int
	for _, val := range s.Split(input, " ") {
		v, err := strconv.Atoi(val)
		if err != nil {panic(err)}
		in = append(in, v)
	}
	_, ret = check(in)

	fmt.Println("Part 1:", ret)
}

func part2() {
	ret := 0
	input := getInput()[0]
	var in []int
	for _, val := range s.Split(input, " ") {
		v, err := strconv.Atoi(val)
		if err != nil {panic(err)}
		in = append(in, v)
	}
	_, ret = check2(in)

	fmt.Println("Part 2:", ret)
}