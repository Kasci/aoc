package main

import (
	"fmt"
	"os"
	"slices"
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

func main() {
	part1()
	part2()
}

func inc(current int, arr []int) int {
	current++
	return current % len(arr)
}

func dec(current int, arr []int) int {
	current += len(arr)-1
	return current % len(arr)
}

func moveRight(current int, arr []int) int {
	current = inc(current, arr)
	for {
		if arr[current] != -1 {break}
		current = inc(current, arr)
	}
	return current
}

func moveLeft(current int, arr []int) int {
	current = dec(current, arr)
	for {
		if arr[current] != -1 {break}
		current = dec(current, arr)
	}
	return current
}


func simulate(players int, last int) int {
	ret := 0

	var pla []int
	for range players {
		pla = append(pla, 0)
	}

	var arr []int
	current := 1
	arr = append(arr, 0, 1)
	i := 2
	for range last-1 {
		if i % 23 == 0 {
			for range 7 {
				current = moveLeft(current, arr)
			}
			val := arr[current]
//			arr = rmv(arr, val)
			arr[current] = -1
			current = moveRight(current, arr)
			pla[i%players] += i+val
		} else {
			for range 2 {
				current = moveRight(current, arr)
			}
			arr = slices.Insert(arr, current, i)
		}
		if i % 100000 == 0 {
			fmt.Println(i)
		}
		i++
	}
	for _, p := range pla {
		if p > ret {
			ret = p
		}
	}
	return ret
}

type node struct {
	value int
	next *node
	previous *node
}

func simulate2(players int, last int) int {
	ret := 0

	var pla []int
	for range players {
		pla = append(pla, 0)
	}

	nZero := node{value: 0}
	nOne := node{value: 1, previous: &nZero, next: &nZero}
	nZero.next = &nOne
	nZero.previous = &nOne
	length := 2
	current := &nOne
	i := 2
	for range last-1 {
		if i % 23 == 0 {
			for range 7 {
				current = current.previous
			}
			pla[i%players] += i+current.value
			next := current.next
			previous := current.previous
			next.previous = previous
			previous.next = next
			current = current.next
		} else {
			current = current.next
			next := current.next
			newNode := &node{value: i, previous: current, next: next}
			current.next = newNode
			next.previous = newNode
			current = newNode
			length++
		}
		i++
//		tmp := &nZero
//		for {
//			fmt.Printf("%d ", tmp.value)
//			tmp = tmp.next
//			if tmp.value == nZero.value {break}
//		}
//		fmt.Println()
	}
	for _, p := range pla {
		if p > ret {
			ret = p
		}
	}
	return ret
}

func part1() {
	ret := 0
	input := getInput()[0]
	spl := s.Split(input, " ")
	_p, _l := spl[0], spl[6]
	players, err := strconv.Atoi(_p)
	if err != nil {panic(err)}
	last, err := strconv.Atoi(_l)
	if err != nil {panic(err)}

	ret = simulate2(players, last)

	fmt.Println("Part 1:", ret)
}

func part2() {
	ret := 0
	input := getInput()[0]
	spl := s.Split(input, " ")
	_p, _l := spl[0], spl[6]
	players, err := strconv.Atoi(_p)
	if err != nil {panic(err)}
	last, err := strconv.Atoi(_l)
	if err != nil {panic(err)}

	ret = simulate2(players, last*100)


	fmt.Println("Part 2:", ret)
}