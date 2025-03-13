#include <iostream>;
#include <iomanip>;
#include <cmath>;

int main()
{
  double cantidad, interes;
  int anios;

  std::cout << "Ingrese la cantidad a invertir: $";
  std::cin >> cantidad;

  std::cout << "Ingrese el interes anual: ";
  std::cin >> interes;

  std::cout << "Ingrese el numero de anios: ";
  std::cin >> anios;

  std::cout << std::fixed << std::setprecision(2);

  for (int i = 0; i < anios; i++)
  {
    cantidad = cantidad + (cantidad * (interes / 100.0));
    std::cout << "En un anio tu capital obtenido sera: $" << cantidad << std::endl;
  }

  return 0;
}