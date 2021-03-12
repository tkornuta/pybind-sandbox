#include "my_math_ext.hpp"
#include <ctime>
#include <iostream>
#include <string>

void print_localtime() {
  std::time_t result = std::time(nullptr);
  std::cout << std::asctime(std::localtime(&result));
}

int main(int argc, char** argv) {
  std::cout << "Add: " << add(1,2) << std::endl;
  print_localtime();
  return 0;
}