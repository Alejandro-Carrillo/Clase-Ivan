<?php
function obtener_nombre() {
    while (true) {
        $nombre = trim(readline("Ingrese su nombre: "));
        if ($nombre) {
            return $nombre;
        } else {
            echo "El nombre no puede estar vacío. Inténtalo de nuevo.\n";
        }
    }
}

function saludo($nombre) {
    echo "Hola $nombre, bienvenido/a!\n";
}

function main() {
    while (true) {
        $nombre = obtener_nombre();
        saludo($nombre);
        
        $continuar = strtolower(trim(readline("¿Deseas saludar a otra persona? (s/n): ")));
        if ($continuar !== 's') {
            echo "Gracias por usar el programa. ¡Hasta luego!\n";
            break;
        }
    }
}


main();
?>