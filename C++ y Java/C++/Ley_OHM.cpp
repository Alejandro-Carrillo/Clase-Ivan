#include <iostream>
#include <string>
#include <iomanip>

int main()
{
  std::cout << "Calculadora de la Ley de Ohm" << std::endl;
  std::cout << "Selecciona la variable que deseas calcular:" << std::endl;
  std::cout << "1. Voltaje (V)" << std::endl;
  std::cout << "2. Corriente (I)" << std::endl;
  std::cout << "3. Resistencia (R)" << std::endl;

  std::cout << "Ingresa el numero de la opcion (1, 2 o 3): ";
  std::string opcion;
  std::getline(std::cin, opcion);

  double corrienteI, resistenciaR, voltajeV;

  if (opcion == "1")
  {
    std::cout << "Ingresa la corriente (I) en amperios: ";
    std::cin >> corrienteI;
    std::cout << "Ingresa la resistencia (R) en ohmios: ";
    std::cin >> resistenciaR;
    voltajeV = corrienteI * resistenciaR;
    std::cout << "El voltaje (V) es: " << std::fixed << std::setprecision(2) << voltajeV << " voltios" << std::endl;
  }
  else if (opcion == "2")
  {
    std::cout << "Ingresa el voltaje (V) en voltios: ";
    std::cin >> voltajeV;
    std::cout << "Ingresa la resistencia (R) en ohmios: ";
    std::cin >> resistenciaR;
    corrienteI = voltajeV / resistenciaR;
    std::cout << "La corriente (I) es: " << std::fixed << std::setprecision(2) << corrienteI << " amperios" << std::endl;
  }
  else if (opcion == "3")
  {
    std::cout << "Ingresa el voltaje (V) en voltios: ";
    std::cin >> voltajeV;
    std::cout << "Ingresa la corriente (I) en amperios: ";
    std::cin >> corrienteI;
    resistenciaR = voltajeV / corrienteI;
    std::cout << "La resistencia (R) es: " << std::fixed << std::setprecision(2) << resistenciaR << " ohmios" << std::endl;
  }
  else
  {
    std::cout << "Opcion no valida. Por favor, selecciona 1, 2 o 3." << std::endl;
  }

  return 0;
}