<?php
$num1 = 10;
$num2 = 5;

function suma($num1, $num2) {
    $sum = $num1 + $num2;
    echo "Resultado de la suma: $sum\n";
}
suma($num1, $num2);

function resta($num1, $num2) {
    $rest = $num1 - $num2;
    echo "Resultado de la resta: $rest\n";
}
resta($num1, $num2);

function multiplicacion($num1, $num2) {
    $mult = $num1 * $num2;
    echo "Resultado de la multiplicación: $mult\n";
}
multiplicacion($num1, $num2);

function division($num1, $num2) {
    if ($num2 != 0) {
        $div = $num1 / $num2;
        echo "Resultado de la división: $div\n";
    } else {
        echo "No se puede dividir entre cero\n";
    }
}
division($num1, $num2);

function potencia($num1, $num2) {
    $pot = pow($num1, $num2);
    echo "Resultado de la potencia: $pot\n";
}
potencia($num1, $num2);
?>