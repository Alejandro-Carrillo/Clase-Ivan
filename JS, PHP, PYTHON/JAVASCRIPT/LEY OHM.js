function calcularLeyOhm() {
    console.log("Calculadora de la Ley de Ohm");
    console.log("Selecciona la variable que deseas calcular:");
    console.log("1. Voltaje (V)");
    console.log("2. Corriente (I)");
    console.log("3. Resistencia (R)");

    let opcion = prompt("Ingresa el número de la opción (1, 2 o 3):");

    if (opcion === '1') {
        let I = parseFloat(prompt("Ingresa la corriente (I) en amperios:"));
        let R = parseFloat(prompt("Ingresa la resistencia (R) en ohmios:"));
        let V = I * R;
        console.log(`El voltaje (V) es: ${V} voltios`);

    } else if (opcion === '2') {
        let V = parseFloat(prompt("Ingresa el voltaje (V) en voltios:"));
        let R = parseFloat(prompt("Ingresa la resistencia (R) en ohmios:"));
        let I = V / R;
        console.log(`La corriente (I) es: ${I} amperios`);

    } else if (opcion === '3') {
        let V = parseFloat(prompt("Ingresa el voltaje (V) en voltios:"));
        let I = parseFloat(prompt("Ingresa la corriente (I) en amperios:"));
        let R = V / I;
        console.log(`La resistencia (R) es: ${R} ohmios`);

    } else {
        console.log("Opción no válida. Por favor, selecciona 1, 2 o 3.");
    }
}

calcularLeyOhm();