#include <iostream>

int main() {
    int a,b,c,d,e;
    std::cin>>a>>b>>c>>d>>e;
    std::cout<<(a*a+b*b+c*c+d*d+e*e)%10;
}