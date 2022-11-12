#include <iostream>

int main() {
    int number;
    int i;
    int j;
    int r1 = 0;
    int r2 = 0;
    std::cout<<"Введите размер массвиа:";
    std::cin>>number;
    int** array = new int*[number];
    for (i = 0; i < number; i++){
        array[i] = new int(number);
        for (j = 0; j < number; j++){
                std::cout<<"Введите число:";
                std::cin>>array[i][j];
        }
    }
    
    for(i = 0; i < number; i++){
        r1 += array[i][i];
    }
    
    for(i = 0; i < number; i++){
        r2 += array[i][number - 1 - i];
    }
    std::cout<<r1<<std::endl;
    std::cout<<r2<<std::endl;
    return 0;
}


// #include <iostream>
// using namespace std;

// void print_array(int** ar, int m, int n) {
//     for (int i = 0; i < m; ++i) {
//         for (int j = 0; j < n; ++j) {
//             cout << ar[i][j]<<" ";
//         }
//         cout << endl;
//     }
// }
// int main()
// {
//     int size;
//     cout << "enter the size of the array: ";
//     cin >> size;
//     int** array = new int* [size];
//     for (int i = 0; i < size; ++i) {
//         array[i] = new int(size);
//         for (int j = 0; j < size; ++j) {
//             cout << "enter array element: ";
//             cin >> array[i][j];
//         }
//     }
//     print_array(array, size, size);
//     return 0;
    
// }
