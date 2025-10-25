#include <iostream>
#include <iomanip>
#include <array>

int main() {
    std::array<int,30> a;
    std::array<int,28> b;
    std::array<int,2> c{0,0};
    for (int i{0}; i<30; i++) {
        a[i]=i+1;
    }
    for (int i{0}; i<28; i++) {
        std::cin>>b[i];
    }
    for (int i : a) {
        int t{0};
        for (int j : b) {
            if (i==j) {
                t=1;
            }
        }
        if (t==0) {
            if (c[0]==0) {
                c[0]=i;
            }
            else {
                c[1]=i;
            }
        }
    }
    for (int i{0}; i<2; i++) {
        std::cout<<c[i]<<std::endl;
    }
}