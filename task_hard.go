package main

import (
	"errors"
	"fmt"
)

type IntDeque struct {
	items []int
}

func NewIntDeque() *IntDeque {
	return &IntDeque{
		items: make([]int, 0),
	}
}

func (a *IntDeque) IsEmpty() bool {
	return len(a.items) == 0
}

func (a *IntDeque) Size() int {
	return len(a.items)
}

func (a *IntDeque) Clear() {
	a.items = make([]int, 0)
}

func (a *IntDeque) PopBack() (int, error) {
	if a.IsEmpty() {
		return 0, errors.New("Ошибка: дек пуст")
	}
	last_ind := len(a.items) - 1
	item := a.items[last_ind]
	a.items = a.items[:last_ind]
	return item, nil
}

func (a *IntDeque) PopFront() (int, error) {
	if a.IsEmpty() {
		return 0, errors.New("Ошибка: дек пуст")
	}
	item := a.items[0]
	a.items = a.items[1:]
	return item, nil
}

func (a *IntDeque) PushBack(num int) {
	a.items = append(a.items, num)
}

func (a *IntDeque) PushFront(num int) {
	a.items = append([]int{num}, a.items...)
}

func main() {
	// создание дека
	deque := NewIntDeque()

	// проверка: пустой ли дек
	fmt.Println("условие: дек пуст -", deque.IsEmpty())

	// длина дека
	fmt.Println("длина дека -", deque.Size())

	// добавление элементов в дек
	deque.PushBack(10)
	deque.PushBack(20)
	deque.PushFront(100)

	fmt.Println("элементы дека:", deque)

	// проверка: пустой ли дек
	fmt.Println("условие: дек пуст -", deque.IsEmpty())

	// длина дека
	fmt.Println("длина дека -", deque.Size())

	// удаление и присвоение последнего элемента дека
	a, _ := deque.PopBack()
	fmt.Println("последний элемент дека -", a)

	fmt.Println("элементы дека:", deque)
	fmt.Println("длина дека -", deque.Size())

	// удаление и присвоение первого элемента дека
	a, _ = deque.PopFront()
	fmt.Println("первый элемент дека -", a)

	fmt.Println("элементы дека:", deque)
	fmt.Println("длина дека -", deque.Size())

	// очистка дека
	deque.Clear()
	fmt.Println("элементы дека:", deque)
	fmt.Println("условие: дек пуст -", deque.IsEmpty())

	// попытка вызова PopBack() и PopFront() для пустого дека
	b, err := deque.PopBack()
	fmt.Println("последний элемент дека -", b)
	fmt.Println("статус ошибки -", err)
	b, err = deque.PopFront()
	fmt.Println("первый элемент дека -", b)
	fmt.Println("статус ошибки -", err)
}
