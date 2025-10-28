package main

import (
	"errors"
	"fmt"
)

type IntStack struct {
	items []int
}

func NewIntStack() *IntStack {
	return &IntStack{
		items: make([]int, 0),
	}
}

func (a *IntStack) Push(num int) {
	a.items = append(a.items, num)
}

func (a *IntStack) IsEmpty() bool {
	return len(a.items) == 0
}

func (a *IntStack) Size() int {
	return len(a.items)
}

func (a *IntStack) Clear() {
	a.items = make([]int, 0)
}

func (a *IntStack) Pop() (int, error) {
	if a.IsEmpty() {
		return 0, errors.New("Ошибка: стек пуст")
	}
	last_ind := len(a.items) - 1
	item := a.items[last_ind]
	a.items = a.items[:last_ind]
	return item, nil
}

func main() {
	// создание стека
	stack := NewIntStack()

	// проверка: пустой ли стек
	fmt.Println("условие: стек пуст -", stack.IsEmpty())

	// длина стека
	fmt.Println("длина стека -", stack.Size())

	// добавление элементов в стек
	stack.Push(10)
	stack.Push(20)
	stack.Push(100)

	fmt.Println("элементы стека:", stack)

	// проверка: пустой ли стек
	fmt.Println("условие: стек пуст -", stack.IsEmpty())

	// длина стека
	fmt.Println("длина стека -", stack.Size())

	// удаление и присвоение последнего элемента стека
	a, _ := stack.Pop()
	fmt.Println("последний элемент стека -", a)

	fmt.Println("элементы стека:", stack)
	fmt.Println("длина стека -", stack.Size())

	// очистка стека
	stack.Clear()
	fmt.Println("элементы стека:", stack)
	fmt.Println("условие: стек пуст -", stack.IsEmpty())

	// попытка вызова Pop() для пустого стека
	b, err := stack.Pop()
	fmt.Println("последний элемент стека -", b)
	fmt.Println("статус ошибки -", err)
}
