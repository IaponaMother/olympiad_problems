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
