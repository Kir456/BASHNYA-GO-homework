package main

import (
	"fmt"
)

func main() {
	var num int
	fmt.Scan(&num)

	ok := 0
	if num >= 12307 {
		fmt.Println("Ошибка: число слишком большое")
		ok = 1
	}

	for num < 12307 {
		if num < 0 {
			num = -num
		} else if num%7 == 0 {
			num *= 39
		} else if num%9 == 0 {
			num = num*13 + 1
			continue
		} else {
			num = (num + 2) * 3
		}

		if (num%13 == 0) && (num%9 == 0) {
			fmt.Println("service error")
			ok = 1
			break
		} else {
			num += 1
		}
	}

	if ok == 0 {
		fmt.Println("В результате получили число", num)
	}
}
