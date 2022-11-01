#include <math.h>
#include <iostream>
#include <string>

void func(int n){
    for (int k = 1; k <= n; k++){
        for(int i = 1; i <= n; i++){
            for(int j = 1; j <= n; j++){
                if(sqrt(i) + sqrt(j) == sqrt(k)){
                    std::string s1 = std::to_string(i);
                    std::string s2 = std::to_string(j);
                    std::string s3 = std::to_string(k);
                    std::cout<<s1 + " " + s2 + " при n = " + s3<<std::endl;
                }
            }
        }
    
    }
}

int main()
{   
    int number = 0;
    std::cout<<"enter the number: ";
    std::cin>>number;
    func(number);

    return 0;
}
