#include <iostream>
#include <string>

int main()
{
  std::string palabra;

  std::cout << "Ingrese la palabra que quiere que se repita: ";
  std::getline(std::cin, palabra);

  for (int i = 0; i < 10; i++)
  {
    std::cout << palabra << std::endl;
  }

  return 0;
}