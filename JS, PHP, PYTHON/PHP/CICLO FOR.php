<?php
function inversion() {
    $cant = (float)readline("Ingrese la cantidad a invertir: $");
    $inter = (float)readline("Ingrese el interés anual: ");
    $años = (int)readline("Ingrese el número de años: ");
    
    for ($i = 0; $i < $años; $i++) {
        $cant += $cant * ($inter / 100);
        echo "En un año tu capital obtenido será: $" . number_format($cant, 2) . "\n";
    }
}

inversion();
?>