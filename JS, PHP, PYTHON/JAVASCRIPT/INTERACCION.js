function adivinaElNumero() {
    const num = Math.floor(Math.random() * 10) + 1; // Genera un número aleatorio entre 1 y 10
    let adivinar = parseInt(prompt("Adivina el número del 1 al 10:"));

    if (num === adivinar) {
        console.log("Has ganado");
    } else {
        console.log("Has perdido, el número era: " + num);
    }
}

adivinaElNumero();