#include <iostream>
#include <iomanip>
#include <vector>

int main() {
    int n,x;
    std::cin>>n>>x;
    std::vector<int> a(n);
    for (int i{0}; i<n; i++) {
        std::cin>>a[i];
    }
    for (int i : a) {
        if (i<x) {
            std::cout<<i<<" ";
        }
    }
}