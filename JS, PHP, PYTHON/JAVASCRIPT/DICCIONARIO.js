const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

const diccionario = {
    'Euro': '€',
    'Dollar': '$',
    'Yen': '¥',
    'Peso': '$'
};

function verSigno() {
    readline.question("Ingrese el tipo de divisa: ", divisaInput => {
        let divisa = divisaInput.charAt(0).toUpperCase() + divisaInput.slice(1).toLowerCase();

        if (diccionario[divisa]) {
            console.log("Este es el sino de la divisa:", diccionario[divisa]);
        } else {
            console.log("Divisa no encontrada.");
        }
        readline.close();
    });
}

verSigno();