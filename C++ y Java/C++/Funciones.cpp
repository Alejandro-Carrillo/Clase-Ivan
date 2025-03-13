#include <iostream>
#include <string>
#include <cctype>

std::string obtenerNombre()
{
  std::string nombre;
  while (true)
  {
    std::cout << "Ingrese su nombre: ";
    std::getline(std::cin, nombre);
    size_t first = nombre.find_first_not_of(' ');
    if (std::string::npos == first)
    {
      nombre = "";
    }
    else
    {
      size_t last = nombre.find_last_not_of(' ');
      nombre = nombre.substr(first, (last - first + 1));
    }

    if (!nombre.empty())
    {
      return nombre;
    }
    else
    {
      std::cout << "El nombre no puede estar vacío. Inténtalo de nuevo." << std::endl;
    }
  }
}

void saludar(const std::string &nombre)
{
  std::cout << "Hola " << nombre << ", bienvenido!" << std::endl;
}

int main()
{
  while (true)
  {
    std::string nombre = obtenerNombre();
    saludar(nombre);

    std::string continuar;
    std::cout << "Deseas saludar a otra persona? (s/n): ";
    std::getline(std::cin, continuar);

    size_t first = continuar.find_first_not_of(' ');
    if (std::string::npos == first)
    {
      continuar = "";
    }
    else
    {
      size_t last = continuar.find_last_not_of(' ');
      continuar = continuar.substr(first, (last - first + 1));
    }
    for (char &c : continuar)
    {
      c = std::tolower(c);
    }

    if (continuar != "s")
    {
      std::cout << "Gracias por usar el programa. Hasta luego!" << std::endl;
      break;
    }
  }

  return 0;
}