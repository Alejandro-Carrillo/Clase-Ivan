<?php
$lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"];

$materias = $lista;

function mostrar($materias) {
    echo "Yo estudio " . count($materias) . " materias\n";
    echo "Las materias son: " . implode(", ", $materias) . "\n";
}

mostrar($materias);
?>