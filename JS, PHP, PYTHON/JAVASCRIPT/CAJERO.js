const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

function cajero() {
    console.log("Bienvenido al cajero");
    let saldo = 1000;

    function mostrarMenu() {
        console.log("1. Ingresar dinero");
        console.log("2. Retirar dinero");
        console.log("3. Ver saldo");
        console.log("4. Salir");
        console.log("------------------------");
        readline.question("¿Qué deseas hacer? ", opcion => {
            manejarOpcion(opcion);
        });
    }

    function manejarOpcion(opcion) {
        console.log("");
        console.log("------------------------");
        console.log("");
        console.log(`Has seleccionado la opción: ${opcion}`);

        if (opcion === "1") {
            readline.question("¿Cuánto dinero deseas ingresar? $", monto => {
                monto = parseFloat(monto);
                if (!isNaN(monto) && monto > 0) {
                    saldo += monto;
                    console.log(`Se ha ingresado $${monto} a tu cuenta. Tu saldo actual es $${saldo}`);
                } else {
                    console.log("Monto inválido. Intenta de nuevo.");
                }
                mostrarMenu();
            });
        } else if (opcion === "2") {
            readline.question("¿Cuánto dinero deseas retirar? $", monto => {
                monto = parseFloat(monto);
                if (!isNaN(monto) && monto > 0) {
                    if (monto <= saldo) {
                        saldo -= monto;
                        console.log(`Se ha retirado $${monto} de tu cuenta. Tu saldo actual es $${saldo}`);
                    } else {
                        console.log("No tienes suficiente saldo.");
                    }
                } else {
                    console.log("Monto inválido. Intenta de nuevo.");
                }
                mostrarMenu();
            });
        } else if (opcion === "3") {
            console.log(`Tu saldo actual es $${saldo}`);
            mostrarMenu();
        } else if (opcion === "4") {
            console.log("Gracias por utilizar el cajero");
            readline.close();
        } else {
            console.log("Opción no válida. Por favor, intenta de nuevo.");
            mostrarMenu();
        }
    }

    mostrarMenu();
}

cajero();