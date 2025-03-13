#include <iostream>;
#include <string>;

int main()
{
  int saldo = 1000;
  std::string opcion;
  double monto;

  std::cout << "Bienvenido al cajero" << std::endl;

  while (true)
  {
    std::cout << "1. Ingresar dinero" << std::endl;
    std::cout << "2. Retirar dinero" << std::endl;
    std::cout << "3. Ver saldo" << std::endl;
    std::cout << "4. Salir" << std::endl;

    std::cout << "¿Que deseas hacer? ";
    std::getline(std::cin, opcion);

    if (opcion == "1")
    {
      std::cout << "¿Cuanto dinero deseas ingresar? $";
      std::cin >> monto;
      std::cin.ignore(); // Consumir la nueva línea pendiente
      saldo += monto;
      std::cout << "Se ha ingresado $" << monto << " a tu cuenta. Tu saldo actual es $" << saldo << std::endl;
    }
    else if (opcion == "2")
    {
      std::cout << "¿Cuanto dinero deseas retirar? $";
      std::cin >> monto;
      std::cin.ignore(); // Consumir la nueva línea pendiente
      if (monto <= saldo)
      {
        saldo -= monto;
        std::cout << "Se ha retirado $" << monto << " de tu cuenta. Tu saldo actual es $" << saldo << std::endl;
      }
      else
      {
        std::cout << "Saldo insuficiente." << std::endl;
      }
    }
    else if (opcion == "3")
    {
      std::cout << "Tu saldo actual es $" << saldo << std::endl;
    }
    else if (opcion == "4")
    {
      std::cout << "Gracias por utilizar el cajero" << std::endl;
      break; // Sale del bucle while, terminando el programa
    }
    else
    {
      std::cout << "Opción no válida. Por favor, intenta de nuevo." << std::endl;
    }
  }

  return 0;
}