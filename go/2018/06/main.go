package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	s "strings"
)

const N = 400

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

func getDist(point [2]int, c [2]int) int {
	dx := int(math.Abs(float64(point[0]-c[0])))
	dy := int(math.Abs(float64(point[1]-c[1])))
	return dx+dy
}

func getClosest(point [2]int, coords [][2]int) []int {
	minDist := 9999999
	minId := []int{}
	for i, c := range coords {
		dist := getDist(point, c)
		if dist < minDist {
			minDist = dist
			minId = []int{i}
		} else if dist == minDist {
			minId = append(minId, i)
		}
	}
	return minId
}

func countClosest(point int, coords [][2]int) int {
	count := 0
	for i := range N {
		for j := range N {
			cl := getClosest([2]int{i,j}, coords)
			if len(cl) == 1 && cl[0] == point {count++}
		}
	}
	return count
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

func part1() {
	ret := 0
	input := getInput()
	var coords [][2]int
	for _, val := range input {
		k := s.Split(val, ", ")
		x, err := strconv.Atoi(k[0])
		if err != nil {panic(err)}
		y, err := strconv.Atoi(k[1])
		if err != nil {panic(err)}
		coords = append(coords, [2]int{x,y})
	}

	var infinite []int
	for i := range N {
		closest := getClosest([2]int{0,i}, coords)
		if len(closest) == 1 {
			infinite = apnd(infinite, closest[0])
		}
		closest = getClosest([2]int{i,0}, coords)
		if len(closest) == 1 {
			infinite = apnd(infinite, closest[0])
		}
		closest = getClosest([2]int{N-1,i}, coords)
		if len(closest) == 1 {
			infinite = apnd(infinite, closest[0])
		}
		closest = getClosest([2]int{i,N-1}, coords)
		if len(closest) == 1 {
			infinite = apnd(infinite, closest[0])
		}
	}
	maxSize := 0
	for i, _ := range coords {
		if contain(infinite, i) {continue}
		size := countClosest(i, coords)
		if size > maxSize {
			maxSize = size
		}
	}
	ret = maxSize

	fmt.Println("Part 1:", ret)
}

func part2() {
	ret := 0
	input := getInput()
	var coords [][2]int
	for _, val := range input {
		k := s.Split(val, ", ")
		x, err := strconv.Atoi(k[0])
		if err != nil {panic(err)}
		y, err := strconv.Atoi(k[1])
		if err != nil {panic(err)}
		coords = append(coords, [2]int{x,y})
	}

	for i := range N {
		for j := range N {
			n := 0
			for _, c := range coords {
				n += getDist([2]int{i,j}, c)
			}
			if n < 10000 {ret++}
		}
	}

	fmt.Println("Part 2:", ret)
}