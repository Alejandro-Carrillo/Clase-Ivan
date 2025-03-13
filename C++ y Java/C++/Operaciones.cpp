#include <iostream>
#include <cmath>

int num1 = 10;
int num2 = 5;

void suma()
{
  int sum = num1 + num2;
  std::cout << "Resultado de la suma: " << sum << std::endl;
}

void resta()
{
  int rest = num1 - num2;
  std::cout << "Resultado de la resta: " << rest << std::endl;
}

void multiplicacion()
{
  int mult = num1 * num2;
  std::cout << "Resultado de la multiplicacion: " << mult << std::endl;
}

void division()
{
  if (num2 != 0)
  {
    double div = static_cast<double>(num1) / num2;
    std::cout << "Resultado de la division: " << div << std::endl;
  }
  else
  {
    std::cout << "No se puede dividir entre cero" << std::endl;
  }
}

void potencia()
{
  double pot = std::pow(num1, num2);
  std::cout << "Resultado de la potencia: " << pot << std::endl;
}

int main()
{
  suma();
  resta();
  multiplicacion();
  division();
  potencia();

  return 0;
}