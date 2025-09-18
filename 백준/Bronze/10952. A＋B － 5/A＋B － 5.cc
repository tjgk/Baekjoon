#include <iostream>

int main() {
    int a,b;
    while (1) {
        std::cin >> a >> b;
        if (a==0 and b==0) {
            break;
        }
        else {
            std::cout << a+b << std::endl;
        }
    }
}