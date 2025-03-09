const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
})


function tabla() {
    let continuar = 1;
    readline.question("Ingrese Ingrese un número para conocer la tabla de multiplicar:", input => {
        let num = parseInt(input);
        while (continuar === 1) {
            if (!isNaN(num)) {
                for (let i = 1; i <= 10; i++) {
                    console.log(`${num} x ${i} = ${num * i}`);
                }
                continuar = 0;
                readline.close();
                break;
                // Salir del bucle después de mostrar la tabla
            } else {
                console.log("Error, por favor ingrese un número entero");
            }
        }
    })
}

tabla();