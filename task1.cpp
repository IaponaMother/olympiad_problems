// #include <iostream>

// using namespace std;

// int main()
// {
//     int* a = new int[2];
//     for (int i = 0; i < 2; i++){
//         cin>>a[i];
//     }
    
//     if (a[1] - a[0] == 1) cout<<a[0];
//     else{
//         if(a[1] <= a[0]){
//             if (a[0] % a[1] == 0) cout<<0;
//             else cout<<a[0] * a[1];
            
//         }
//         else{
//             if (a[1] % a[0] == 0) cout<<(a[1] / a[0] - 1) * a[0];
//             else cout<<a[0] * a[1];
//         }
            
//         }
        
//     }

#include <iostream>

using namespace std;

int main()
{
    int* a = new int[3];
    for (int i = 0; i < 3; i++){
        cin>>a[i];
    }
    int n = a[0];
    int k = a[1];
    int p = a[2];
    
    
    for(int i = 0; i < n; i++){
        cin>>a[i];
    }
    
    for(int i = 0; i < n; i+=k){
        if(p + a[i] < 0){
            p = -1;
            break;
        }
        
        else{
            p += a[i];
        }
    }
    cout<<p;
}
