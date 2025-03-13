#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <iomanip>

std::vector<std::vector<bool>> generarCombinaciones(int numVariables)
{
  std::vector<std::vector<bool>> combinaciones;
  int numCombinaciones = static_cast<int>(std::pow(2, numVariables));

  for (int i = 0; i < numCombinaciones; i++)
  {
    std::vector<bool> combinacion;
    for (int j = numVariables - 1; j >= 0; j--)
    {
      bool valor = (i & (1 << j)) != 0;
      combinacion.push_back(valor);
    }
    combinaciones.push_back(combinacion);
  }
  return combinaciones;
}

int main()
{
  std::vector<std::string> variables = {"A", "B"};
  std::vector<std::vector<bool>> combinaciones = generarCombinaciones(variables.size());

  for (const std::string &var : variables)
  {
    std::cout << std::left << std::setw(6) << var << " | ";
  }
  std::cout << "A AND B" << std::endl;

  std::cout << std::string(variables.size() * 8 + 7, '-') << std::endl;

  for (const std::vector<bool> &combinacion : combinaciones)
  {
    bool A = combinacion[0];
    bool B = combinacion[1];
    bool resultado = A && B;

    std::cout << std::left << std::setw(6) << std::boolalpha << A << " | ";
    std::cout << std::left << std::setw(6) << std::boolalpha << B << " | ";
    std::cout << std::left << std::setw(6) << std::boolalpha << resultado << std::endl;
  }

  return 0;
}