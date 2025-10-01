#include <iostream>
#include <vector>

int main () {
    int n,t;
    int s{0};
    std::vector<int> a;
    std::cin>>n;
    for (int i{0}; i<n; i++) {
        std::cin>>t;
        a.push_back(t);
    }
    int v;
    std::cin>>v;
    for (int c : a) {
        if (c==v) {
            s+=1;
        }
    }
    std::cout<<s;
}