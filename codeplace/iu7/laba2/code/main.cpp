#include <chrono>
#include <iostream>
#include <fstream>
#include <vector>
#include <random>
#include <sstream>

using namespace std;
using namespace chrono;

struct InputError : public exception {
    string message;
    InputError(const string& msg) : message(msg) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
};

struct FileError : public exception {
    string message;
    FileError(const string& msg) : message(msg) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
};

struct IntTypeError : public exception {
    string message;
    IntTypeError(const string& msg) : message(msg) {}
    const char* what() const noexcept override {
        return message.c_str();
    }
};

void recursive() {
    int number;
    cin >> number;
    if (cin.fail()) {
        cin.clear();
        cin.ignore(numeric_limits<streamsize>::max(), '\n');
        throw InputError("Ошибка: неправильный ввод");
    }
    else if (number < 0) {
        throw IntTypeError("Ошибка: введено отрицательное число");
    }
    else if (number > 0) {
        if (number % 2 == 1) {
            cout << number << endl;
        }
        recursive();
    }
}

void classic() {
    int number;
    while (1) {
        cin >> number;
        if (cin.fail()) {
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
            throw InputError("Ошибка: неправильный ввод");
        }
        else if (number == 0) {
            break;
        }
        else if (number < 0) {
            throw IntTypeError("Ошибка: введено отрицательное число");
        }
        else if (number % 2 == 1) {
            cout << number << endl;
        }
    }
}

void benchmark() {
    const int NUM_TESTS = 100;
    const int SEQUENCE_LENGTH = 9000;

    ofstream file("data.txt", ios::app);
    if (!file.is_open()) {
        throw FileError("Ошибка: не удалось открыть файл");
    }
    
    random_device rand;
    mt19937 generate(rand());
    uniform_int_distribution<int> dist(1, 1000);
    
    vector<long long> recursive_times;
    vector<long long> classic_times;
    
    cout << "Количество тестов: " << NUM_TESTS << endl;
    cout << "Длина последовательности: " << SEQUENCE_LENGTH+1 << endl;
    
    for (int test = 0; test < NUM_TESTS; ++test) {
        vector<int> test_data;
        for (int i = 0; i < SEQUENCE_LENGTH; ++i) {
            test_data.push_back(dist(generate));
        }
        test_data.push_back(0);
        
        {
            auto orig_cin = cin.rdbuf();
            
            stringstream test_stream;
            for (int num : test_data) {
                test_stream << num << " ";
            }
            
            cin.rdbuf(test_stream.rdbuf());
            
            auto start = high_resolution_clock::now();
            recursive();
            auto end = high_resolution_clock::now();
            
            cin.rdbuf(orig_cin);
            
            duration<double, milli> time = end - start;
            recursive_times.push_back(time.count());
        }
        
        {
            auto orig_cin = cin.rdbuf();
            
            stringstream test_stream;
            for (int num : test_data) {
                test_stream << num << " ";
            }
            
            cin.rdbuf(test_stream.rdbuf());
            
            auto start = high_resolution_clock::now();
            classic();
            auto end = high_resolution_clock::now();
            
            cin.rdbuf(orig_cin);
            
            duration<double, milli> time = end - start;
            classic_times.push_back(time.count());
        }
    }
    
    long long recursive_avg = 0, classic_avg = 0;
    for (int i = 0; i < NUM_TESTS; ++i) {
        recursive_avg += recursive_times[i];
        classic_avg += classic_times[i];
    }
    recursive_avg /= NUM_TESTS;
    classic_avg /= NUM_TESTS;
    
    cout << "Результаты замера времени" << endl;
    cout << "Рекурсивная версия: " << recursive_avg << "(мс)" << endl;
    cout << "Классическая версия: " << classic_avg << "(мс)" << endl;
    file << recursive_avg << " " << classic_avg << endl;
}

int main() {
    cout << "Выберите режим работы\n" << "Введите соответствующий номер" << endl;
    cout << "1) Пользовательский ввод последовательностей\n" << "2) Автоматический массированный замер времени работы алгоритмов" << endl;

    try {
        int n;
        cin >> n;
        if (n == 1) {
            cout << "Введите последовательность натуральных чисел, завершающуюся 0" << endl;
            
            cout << "Рекурсивная версия:" << endl;
            recursive();

            cout << "Введите последовательность еще раз" << endl;
            cout << "Классическая версия:" << endl;
            classic();
        }
        else if (n == 2) {
            benchmark();
        }
        else {
            throw InputError("Ошибка: неправильный ввод");
        }
    }
    catch (const InputError& e) {
        cerr << e.what() << endl;
        return 1;
    }
    catch (const IntTypeError& e) {
        cout << e.what() << endl;
        return 1;
    }
    catch (const exception& e) {
        cerr << "Неизвестная ошибка: " << e.what() << endl;
        return 1;
    }
}