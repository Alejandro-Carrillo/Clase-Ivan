const variables = ['A', 'B'];

// Generamos todas las combinaciones de valores booleanos
const combinaciones = [];
for (let i = 0; i < Math.pow(2, variables.length); i++) {
    combinaciones.push([(i & 2) !== 0, (i & 1) !== 0]);
}

// Imprimimos la cabecera de la tabla
console.log(`${variables.join(' | ')} | A AND B`);
console.log('-'.repeat(30));

// Evaluamos la expresión para cada combinación
for (const combinacion of combinaciones) {
    const [A, B] = combinacion;
    const resultado = A && B;
    console.log(`${A} | ${B} | ${resultado}`);
}