<?php
function mostrarPalabra() {
    $palabra = readline("Ingrese la palabra que quiere que se repita: ");
    
    // For para imprimir la palabra 10 veces
    for ($i = 0; $i < 10; $i++) {
        echo $palabra . "\n";
    }
}

mostrarPalabra();
?>