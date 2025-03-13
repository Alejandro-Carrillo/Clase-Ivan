#include <iostream>
#include <map>
#include <string>
#include <algorithm>

std::string capitalizar(std::string str)
{
  if (str.empty())
  {
    return str;
  }
  str[0] = std::toupper(str[0]);
  std::transform(str.begin() + 1, str.end(), str.begin() + 1, ::tolower);
  return str;
}

void conversor(std::map<std::string, std::string> &peso)
{
  std::string divisa;
  std::cout << "Ingrese el tipo de divisa: ";
  std::getline(std::cin, divisa);

  divisa = capitalizar(divisa);

  if (peso.count(divisa) > 0)
  {
    std::cout << "Esta es la divisa: " << peso[divisa] << std::endl;
  }
  else
  {
    std::cout << "Divisa no encontrada." << std::endl;
  }
}

int main()
{
  std::map<std::string, std::string> diccionario;
  diccionario["Euro"] = "€";
  diccionario["Dollar"] = "$";
  diccionario["Yen"] = "¥";
  diccionario["Peso"] = "$";

  conversor(diccionario);

  return 0;
}