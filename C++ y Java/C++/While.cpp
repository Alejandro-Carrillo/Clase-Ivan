#include <iostream>
#include <limits>

int main()
{
  while (true)
  {
    try
    {
      std::cout << "Ingrese un numero para conocer la tabla de multiplicar: ";
      int num;
      std::cin >> num;

      if (std::cin.fail())
      {
        throw std::runtime_error("Entrada invalida");
      }

      for (int i = 1; i <= 10; i++)
      {
        std::cout << num << " x " << i << " = " << (num * i) << std::endl;
      }
      break;
    }
    catch (const std::exception &e)
    {
      std::cerr << "Error, por favor ingrese un numero entero" << std::endl;
      std::cin.clear();
      std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    }
  }

  return 0;
}