#include <iostream>
#include <string>

int main () {
    int t;
    std::cin>>t;
    std::string a;
    for (int i=0; i<t; i++) {
        std::cin>>a;
        std::cout<<a[0]<<a[a.length()-1]<<std::endl;
    }
}