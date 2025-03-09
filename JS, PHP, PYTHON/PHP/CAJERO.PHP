<?php
function cajero() {
    echo "Bienvenido al cajero\n";
    $saldo = 1000;

    // Bucle para conocer las opciones del cajero 
    while (true) {
        echo "1. Ingresar dinero\n";
        echo "2. Retirar dinero\n";
        echo "3. Ver saldo\n";
        echo "4. Salir\n";
        $opcion = readline("¿Qué deseas hacer? ");

        // Opción 1: para ingresar dinero
        if ($opcion == "1") {
            $monto = (float)readline("¿Cuánto dinero deseas ingresar? $");
            $saldo += $monto;
            echo "Se ha ingresado $$monto a tu cuenta. Tu saldo actual es $$saldo\n";
        }
        // Opción 2: para retirar dinero
        elseif ($opcion == "2") {
            $monto = (float)readline("¿Cuánto dinero deseas retirar? $");
            if ($monto <= $saldo) {
                $saldo -= $monto;
                echo "Se ha retirado $$monto de tu cuenta. Tu saldo actual es $$saldo\n";
            } else {
                echo "No tienes suficiente saldo para retirar esa cantidad.\n";
            }
        }
        // Opción 3: para ver el saldo
        elseif ($opcion == "3") {
            echo "Tu saldo actual es $$saldo\n";
        }
        // Opción 4: para salir
        elseif ($opcion == "4") {
            echo "Gracias por utilizar el cajero\n";
            break;
        } else {
            echo "Opción no válida. Por favor, intenta de nuevo.\n";
        }
    }
}

cajero();
?>