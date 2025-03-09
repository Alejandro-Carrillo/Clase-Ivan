const lista = ["Matemáticas", "Física", "Química", "Historia", "Lengua"];

const materias = lista;

function mostrar() {
    console.log(`Yo estudio ${materias.length} materias`);
    console.log(`Las materias son: ${materias.join(', ')}`);
}

mostrar();