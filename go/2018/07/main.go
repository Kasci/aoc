package main

import (
	"fmt"
	"os"
	"sort"
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

func part1() {
	ret := ""
	input := getInput()
	var steps [][]string
	for _, val := range input {
		spl := s.Split(val, " ")
		steps = append(steps, []string{spl[1], spl[7]})
	}

	var fin []string

	var in []string
	var out []string

	for {
		in = nil
		out = nil
		for _, i := range steps {
			in = apnd(in, i[0])
			out = apnd(out, i[1])
		}

		for _, i := range out {
			in = rmv(in, i)
		}
		sort.Strings(in)
		fin = append(fin, in[0])

		for _,i := range fin {
			steps = rmv2(steps, i, func(x []string) string {return x[0]})
		}
		if len(steps) == 0 {
			sort.Strings(out)
			fin = append(fin, out...)
			break
		}
	}
	ret = s.Join(fin, "")

	fmt.Println("Part 1:", ret)
}

type worker struct {
	time int
	finish int
	step string
}

func part2() {
	ret := 0
	input := getInput()
	var steps [][]string
	for _, val := range input {
		spl := s.Split(val, " ")
		steps = append(steps, []string{spl[1], spl[7]})
	}

	var fin []string

	var in []string
	var out []string
	var now []string

	seconds := 0
	const W = 5
	var w [W]worker

	for i := range W {
		w[i] = worker{time: 0, step: "", finish: -1}
	}

	for {
		in = nil
		out = nil
		for _, i := range steps {
			in = apnd(in, i[0])
			out = apnd(out, i[1])
		}
		for _, i := range now {
			in = rmv(in, i)
		}
		for _, i := range out {
			in = rmv(in, i)
		}
		sort.Strings(in)

		for i, _ := range w {
			if w[i].step == "" {
				if len(in) > 0 {
					w[i].time = 0
					w[i].step = in[0]
					w[i].finish = int(in[0][0]-'A'+ 61)
					now = append(now, in[0])
					in = rmv(in, in[0])
				}
			}
		}

		var done []string
		for {
			seconds++
			for i, _ := range w {
				if w[i].step != "" {
					w[i].time++
					if w[i].time == w[i].finish {
						done = append(done, w[i].step)
						now = rmv(now, w[i].step)
						w[i] = worker{time: 0, step: "", finish: -1}
					}
				}
			}
			if len(done) > 0 {break}
		}

		for _,i := range done {
			steps = rmv2(steps, i, func(x []string) string {return x[0]})
			fin = append(fin, i)
		}

		if len(steps) == 0 {
			sort.Strings(out)
			seconds += int(out[0][0]-'A'+61)
			break
		}
	}
	ret = seconds
	fmt.Println("Part 2:", ret)
}