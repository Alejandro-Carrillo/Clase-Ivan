<?php
function tabla() {
    while (true) {
        $input = readline("Ingrese un número para conocer la tabla de multiplicar: ");
        
        if (is_numeric($input) && intval($input) == $input) {
            $num = (int)$input;
            for ($i = 1; $i <= 10; $i++) {
                echo "$num x $i = " . ($num * $i) . "\n";
            }
            break; // Salir del bucle después de mostrar la tabla
        } else {
            echo "Error, por favor ingrese un número entero\n";
        }
    }
}

tabla();
?>