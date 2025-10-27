package main

import (
	"fmt"
	"strconv"
	"unicode/utf8"
)

func main() {
	first := [9]string{"один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять"}
	second := [9]string{"десять", "двадцать", "тридцать", "сорок", "пятьдесят", "шестьдесят", "семьдесят", "восемьдесят", "девяносто"}
	third := [9]string{"сто", "двести", "триста", "четыреста", "пятьсот", "шестьсот", "семьсот", "восемьсот", "девятьсот"}
	second_and_first := [9]string{"одиннадцать", "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать", "девятнадцать"}
	extra_first := [2]string{"одна", "две"}
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
		conv_num := strconv.Itoa(num)
		length := utf8.RuneCountInString(conv_num)
		var string_num string

		word := ""
		if conv_num[length-4] == '1' {
			word = "тысяча"
		} else if conv_num[length-4] == '2' || conv_num[length-4] == '3' {
			word = "тысячи"
		} else {
			word = "тысяч"
		}

		flag := 0
		last := ""
		if conv_num[length-2] == '1' {
			flag = 1
			if conv_num[length-1] == '0' {
				last = second[0]
			} else {
				digit_int := int(conv_num[length-1] - '0')
				last = second_and_first[digit_int-1]
			}
		}

		if flag == 0 {
			for i := length - 1; i >= 0; i-- {
				if conv_num[i] == '0' {
					if length-i == 4 {
						string_num = " " + word + string_num
					}
					continue
				}
				digit_int_for := int(conv_num[i] - '0')
				if (length-i)%3 == 0 {
					string_num = " " + third[digit_int_for-1] + string_num
				} else if (length-i)%3 == 2 {
					string_num = " " + second[digit_int_for-1] + string_num
				} else {
					if length-i == 4 {
						string_num = " " + word + string_num
						if digit_int_for == 1 {
							string_num = " " + extra_first[0] + string_num
						} else if digit_int_for == 2 {
							string_num = " " + extra_first[1] + string_num
						} else {
							string_num = " " + first[digit_int_for-1] + string_num
						}
					} else {
						string_num = " " + first[digit_int_for-1] + string_num
					}
				}
			}
		} else {
			string_num = " " + last
			for i := length - 3; i >= 0; i-- {
				if conv_num[i] == '0' {
					if length-i == 4 {
						string_num = " " + word + string_num
					}
					continue
				}
				digit_int_for := int(conv_num[i] - '0')
				if (length-i)%3 == 0 {
					string_num = " " + third[digit_int_for-1] + string_num
				} else if (length-i)%3 == 2 {
					string_num = " " + second[digit_int_for-1] + string_num
				} else {
					if length-i == 4 {
						string_num = " " + word + string_num
						if digit_int_for == 1 {
							string_num = " " + extra_first[0] + string_num
						} else if digit_int_for == 2 {
							string_num = " " + extra_first[1] + string_num
						} else {
							string_num = " " + first[digit_int_for-1] + string_num
						}
					} else {
						string_num = " " + first[digit_int_for-1] + string_num
					}
				}
			}
		}
		string_num = "-" + string_num
		fmt.Println("В результате получили число", num, string_num)
	}
}
