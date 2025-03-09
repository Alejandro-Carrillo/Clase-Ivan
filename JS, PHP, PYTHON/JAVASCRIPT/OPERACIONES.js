let num1 = 10;
let num2 = 5;

function suma() {
    let sum = num1 + num2;
    console.log("Resultado de la suma:", sum);
}
suma();

function resta() {
    let rest = num1 - num2;
    console.log("Resultado de la resta:", rest);
}
resta();

function multiplicacion() {
    let mult = num1 * num2;
    console.log("Resultado de la multiplicación:", mult);
}
multiplicacion();

function division() {
    if (num2 !== 0) {
        let div = num1 / num2;
        console.log("Resultado de la división:", div);
    } else {
        console.log("No se puede dividir entre cero");
    }
}
division();

function potencia() {
    let pot = num1 ** num2;
    console.log("Resultado de la potencia:", pot);
}
potencia();