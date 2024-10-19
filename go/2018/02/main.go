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
	input := getInput()
	double, tripple := 0,0
	for _, val := range input {
		d,t := 0,0
		for _, v := range s.Split(val, "") {
			if s.Count(val, v) == 2 {d++}
			if s.Count(val, v) == 3 {t++}
		}
		if d > 0 {double++}
		if t > 0 {tripple++}
	}

	ret = double*tripple
	fmt.Println("Part 1:", ret)
}

func part2() {
	input := getInput()
	for i, val := range input {
		for j, vall := range input {
			if i == j {continue}
			diff := 0
			letter := 0
			for k := range len(val) {
				if val[k] != vall[k] {
					letter = k
					diff++
				}
			}
			if diff == 1 {
				ret := s.Split(val, "")
				fmt.Println("Part 2:", s.Join(append(ret[:letter],ret[letter+1:]...),""))
				return
			}
		}
	}

}