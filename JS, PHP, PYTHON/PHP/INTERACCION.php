<?php
function adivinaElNumero() {
    $num = rand(1, 10); // Genera un número aleatorio entre 1 y 10
    $adivinar = (int)readline("Adivina el número del 1 al 10: ");

    if ($num === $adivinar) {
        echo "Has ganado\n";
    } else {
        echo "Has perdido, el número era: $num\n";
    }
}

adivinaElNumero();
?>