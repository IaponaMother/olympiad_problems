#include <iostream>
#include <math.h>

using namespace std;
void len_(float, float, float, float, float, float);
void square();
void perimeter();
void len_(float X1,float Y1,float X2,float Y2,float X3,float Y3, float arr[]){
    float l1;
    float l2;
    float l3;
    l1 = sqrt((X2 - X1) * (X2 - X1) + (Y2 - Y1) * (Y2 - Y1));
    l2 = sqrt((X3 - X1) * (X3 - X1) + (Y3 - Y1) * (Y3 - Y1));
    l3 = sqrt((X2 - X3) * (X2 - X3) + (Y2 - Y3) * (Y2 - Y3));
    arr[0] = l1;
    arr[1] = l2;
    arr[2] = l3;
}

void square(float arr[]){
    float s;
    float p;
    p = (arr[0] + arr[1] + arr[2])/2;
    s = sqrt(p * (p - arr[0]) * (p - arr[1]) * (p - arr[2]));
    std::cout<<s<<std::endl;
}

void perimeter(float arr[]){
    float p;
    p = arr[0] + arr[1] + arr[2];
    std::cout<<p<<std::endl;
}

int main()

{
    float x1;
    float y1;
    float x2;
    float y2;
    float x3;
    float y3;
    float array[3] = {0, 0, 0};
    
    std::cout<<"Введите x: ";
    std::cin>> x1;
    std::cout<<"Введите y: ";
    std::cin>> y1;
    std::cout<<"Введите x: ";
    std::cin>> x2;
    std::cout<<"Введите y: ";
    std::cin>> y2;
    std::cout<<"Введите x: ";
    std::cin>> x3;
    std::cout<<"Введите y: ";
    std::cin>> y3;
    



    len_(x1, y1, x2, y2, x3, y3, array);
    perimeter(array);
    square(array);
    return 0;
}
