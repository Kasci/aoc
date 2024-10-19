package main

import (
	"fmt"
	"os"
	r "regexp"
	"slices"
	c "strconv"
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
		a, err := c.Atoi(val)
		if err != nil {panic(err)}
		list[i] = a
	}
	return list
}

func main() {
	part1()
	part2()
}

func getSleepers(input []string) [10000][60]int  {
	var wasSleeping [10000][60]int

	num, err := r.Compile("#([0-9]+)")
	if err != nil {panic(err)}
	time, err := r.Compile(":([0-9]+)]")
	if err != nil {panic(err)}

	current := -1
	start := -1
	for _, val := range input {
		if s.Contains(val, "Guard") {
			current, err = c.Atoi(num.FindStringSubmatch(val)[1])
			if err != nil {panic(err)}
		} else if s.Contains(val, "falls") {
			start, err = c.Atoi(time.FindStringSubmatch(val)[1])
			if err != nil {panic(err)}
		} else if s.Contains(val, "wakes") {
			end, err := c.Atoi(time.FindStringSubmatch(val)[1])
			if err != nil {panic(err)}
			for i := range end-start {
				wasSleeping[current][i+start]++
			}
		}
	}
	return wasSleeping
}

func part1() {
	ret := 0
	input := getInput()
	slices.Sort(input)

	wasSleeping := getSleepers(input)

	maxi, maxn, maxm := 0, 0, 0
	for i := range 10000 {
		n := 0
		m, mm := 0, 0
		for j := range 60 {
			k := wasSleeping[i][j]
			n += k
			if k > m {
				m = k
				mm = j
			}
		}
		if n > maxn {
			maxi = i
			maxn = n
			maxm = mm
		}
	}
	ret = maxi*maxm

	fmt.Println("Part 1:", ret)
}

func part2() {
	ret := 0
	input := getInput()
	slices.Sort(input)

	wasSleeping := getSleepers(input)

	maxi, maxm, maxM := 0, 0, 0
	for i := range 10000 {
		m, mm := 0, 0
		for j := range 60 {
			k := wasSleeping[i][j]
			if k > m {
				m = k
				mm = j
			}
		}
		if m > maxm {
			maxi = i
			maxm = m
			maxM = mm
		}
	}
	ret = maxi*maxM

	fmt.Println("Part 2:", ret)
}