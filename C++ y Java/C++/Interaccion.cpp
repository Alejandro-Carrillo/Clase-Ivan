#include <iostream>
#include <cstdlib>
#include <ctime>

int main()
{

  std::srand(std::time(0));

  int numeroAleatorio = std::rand() % 10 + 1;

  int numeroUsuario;
  std::cout << "Adivina el numero del 1 al 10: ";
  std::cin >> numeroUsuario;

  if (numeroUsuario == numeroAleatorio)
  {
    std::cout << "Has ganado" << std::endl;
  }
  else
  {
    std::cout << "Has perdido, el numero era: " << numeroAleatorio << std::endl;
  }

  return 0;
}