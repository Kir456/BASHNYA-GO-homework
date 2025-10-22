package main

import (
	// "bufio"
	// "os"
	"fmt"
	"strconv"
)

func main() {
	var num int
	fmt.Scan(&num)

	first := num % 10
	second := (num % 100) / 10
	third := num / 100
	var new string
	new = strconv.Itoa(first) + strconv.Itoa(second) + strconv.Itoa(third)
	fmt.Println(new)
}
