<?php
function mayoriaEdad() {
    $edad = (int)readline("Ingresa tu edad: ");
    
    if ($edad >= 18) {
        echo "Eres mayor de edad.\n";
    } else {
        echo "Eres menor de edad.\n";
    }
}

mayoriaEdad();
?>