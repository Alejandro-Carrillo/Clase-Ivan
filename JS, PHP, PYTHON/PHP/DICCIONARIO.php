<?php
$diccionario = array(
    'Euro' => '€',
    'Dollar' => '$',
    'Yen' => '¥',
    'Peso' => '$'
);

function conversor($diccionario) {
    $divisa = ucfirst(trim(readline("Ingrese el tipo de divisa: ")));
    
    if (array_key_exists($divisa, $diccionario)) {
        echo "Esta es la divisa: " . $diccionario[$divisa] . "\n";
    } else {
        echo "Divisa no encontrada.\n";
    }
}

conversor($diccionario);
?>