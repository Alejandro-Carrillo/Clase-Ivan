<?php
// Definimos las variables
$variables = ['A', 'B'];

// Generamos todas las combinaciones de valores booleanos
$combinaciones = [];
for ($i = 0; $i < pow(2, count($variables)); $i++) {
    $combinaciones[] = [($i & 2) !== 0, ($i & 1) !== 0];
}

// Imprimimos la cabecera de la tabla
echo implode(' | ', $variables) . " | A AND B\n";
echo str_repeat('-', 30) . "\n";

// Evaluamos la expresión para cada combinación
foreach ($combinaciones as $combinacion) {
    list($A, $B) = $combinacion;
    $resultado = $A && $B;
    echo "$A | $B | $resultado\n";
}
?>