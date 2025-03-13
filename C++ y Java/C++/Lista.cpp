#include <iostream>
#include <vector>
#include <string>
#include <sstream>

void mostrar(const std::vector<std::string> &materias)
{
  std::cout << "Yo estudio " << materias.size() << " materias" << std::endl;

  std::stringstream ss;
  ss << "[";
  for (size_t i = 0; i < materias.size(); ++i)
  {
    ss << materias[i];
    if (i < materias.size() - 1)
    {
      ss << ", ";
    }
  }
  ss << "]";

  std::cout << "Las materias son: " << ss.str() << std::endl;
}

int main()
{
  std::vector<std::string> materias;
  materias.push_back("Matematicas");
  materias.push_back("Fisica");
  materias.push_back("Quimica");
  materias.push_back("Historia");
  materias.push_back("Lengua");

  mostrar(materias);

  return 0;
}