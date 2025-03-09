const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function inversion() {
    readline.question("Ingrese la cantidad a invertir: $", cantInput => {
        readline.question("Ingrese el interés anual: ", interInput => {
            readline.question("Ingrese el número de años: ", añosInput => {
                let cant = parseFloat(cantInput);
                let inter = parseFloat(interInput);
                let años = parseInt(añosInput, 10);

                for (let i = 0; i < años; i++) {
                    cant += cant * (inter / 100);
                    console.log(`En el año ${i + 1} tu capital obtenido será: $${cant.toFixed(2)}`);
                }
                readline.close();
            });
        });
    });
}

inversion();