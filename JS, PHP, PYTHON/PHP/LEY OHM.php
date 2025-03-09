<?php
function calcularLeyOhm() {
    echo "Calculadora de la Ley de Ohm\n";
    echo "Selecciona la variable que deseas calcular:\n";
    echo "1. Voltaje (V)\n";
    echo "2. Corriente (I)\n";
    echo "3. Resistencia (R)\n";

    $opcion = readline("Ingresa el número de la opción (1, 2 o 3): ");

    if ($opcion == '1') {
        $I = (float)readline("Ingresa la corriente (I) en amperios: ");
        $R = (float)readline("Ingresa la resistencia (R) en ohmios: ");
        $V = $I * $R;
        echo "El voltaje (V) es: $V voltios\n";

    } elseif ($opcion == '2') {
        $V = (float)readline("Ingresa el voltaje (V) en voltios: ");
        $R = (float)readline("Ingresa la resistencia (R) en ohmios: ");
        $I = $V / $R;
        echo "La corriente (I) es: $I amperios\n";

    } elseif ($opcion == '3') {
        $V = (float)readline("Ingresa el voltaje (V) en voltios: ");
        $I = (float)readline("Ingresa la corriente (I) en amperios: ");
        $R = $V / $I;
        echo "La resistencia (R) es: $R ohmios\n";

    } else {
        echo "Opción no válida. Por favor, selecciona 1, 2 o 3.\n";
    }
}

calcularLeyOhm();
?>