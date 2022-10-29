#include <iostream>


using namespace std;

int factorial(int a){
    int r;
    r = 1;
    if(a >= 0){
        int i = 1;
        for(i; i <= a; i++){
            r *= i;
            
        }
    }
    else{
        r = 0;
    }
    return r;
    
}

int func_(int m,int n){
    int r = 0;
    if (m % 2 == 0){
        m += 1;
    }
    for(m; m <= n; m+=2){
        r += factorial(m);
    }
    return r;
}


int main()

{
    int M;
    int N;
    
    std::cout<<"Введите m:  ";
    std::cin>> M;
    std::cout<<"Введите n:   ";
    std::cin>> N;

    std::cout<<func_(M, N)<<std::endl;
    return 0;
}
