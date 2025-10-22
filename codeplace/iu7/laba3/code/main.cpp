#include <iostream>
#include <vector>

using namespace std;

struct InputError : public exception {
    string message;
    InputError(const string& msg) : message(msg) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
};

class FactorialNumber {
    vector<int> num;

    
};

int main() {
    cout << "Выберите вариант взаимодействия с факториальной системой счисления\n" << "Введите соответствующий номер" << endl;
    cout << "1) Сравнение двух чисел" << endl;
    cout << "2) Копирование числа в другую переменную" << endl;
    cout << "3) Сложение двух чисел" << endl;
    cout << "4) Вычитание одного числа из другого" << endl;
    cout << "5) Умножение двух чисел" << endl;
    cout << "6) Остаток от деления одного числа на другое" << endl;

    try {
        int n;
        cin >> n;
        if (n == 1) {

        }
        else if (n == 2) {

        }
        else if (n == 3) {

        }
        else if (n == 4) {

        }
        else if (n == 5) {

        }
        else if (n == 6) {

        }
        else {
            
        }
    }
}