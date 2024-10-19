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

func splitConvert(str string, sep string) (int, int) {
	parts := s.Split(str, sep)
	x, err := strconv.Atoi(parts[0])
	if err != nil {panic(err)}
	y, err := strconv.Atoi(parts[1])
	if err != nil {panic(err)}
	return x,y
}

func part1() {
	ret := 0
	input := getInput()
	const N = 1000
	var fab [N][N]int
	for _, val := range input {
		spl := s.Split(val, " ")
		off, size := spl[2][:len(spl[2])-1], spl[3]
		offX, offY := splitConvert(off, ",")
		sizeX, sizeY := splitConvert(size, "x")
		for i := range sizeX {
			for j := range sizeY {
				fab[offX+i][offY+j]++
			}
		}
	}
	for _, i := range fab {
		for _, j := range i {
			if j > 1 {ret++}
		}
	}

	fmt.Println("Part 1:", ret)
}

func part2() {
	ret := ""
	input := getInput()

	for i, val := range input {
		spl := s.Split(val, " ")
		id, off, size := spl[0], spl[2][:len(spl[2])-1], spl[3]
		offX, offY := splitConvert(off, ",")
		sizeX, sizeY := splitConvert(size, "x")

		overlap := false
		for j, vall := range input {
			if i == j {continue}

			splx := s.Split(vall, " ")
			offx, sizex := splx[2][:len(splx[2])-1], splx[3]
			offXx, offYx := splitConvert(offx, ",")
			sizeXx, sizeYx := splitConvert(sizex, "x")

			if offX < offXx+sizeXx && offX+sizeX > offXx && offY < offYx+sizeYx && offY+sizeY > offYx {
				overlap=true
				break
			}
		}
		if !overlap {
			ret = id[1:]
			break
		}
	}



	fmt.Println("Part 2:", ret)
}