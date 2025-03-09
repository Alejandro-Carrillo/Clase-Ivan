function mostrarPalabra() {
    let palabra = prompt("Ingrese la palabra que quiere que se repita:");
    
    // For para imprimir la palabra 10 veces
    for (let i = 0; i < 10; i++) {
        console.log(palabra);
    }
}

mostrarPalabra();