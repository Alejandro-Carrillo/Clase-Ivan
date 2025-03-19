from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["escuela"]  # Crea la base de datos "escuela"
estudiantes = db["estudiantes"]  # Crea la colección "estudiantes"

# 1. Insertar 5 documentos
estudiantes.insert_many([
    {"nombre": "Ana", "edad": 20, "curso": "Matemáticas", "nota": 8.5},
    {"nombre": "Juan", "edad": 21, "curso": "Física", "nota": 9.2},
    {"nombre": "María", "edad": 19, "curso": "Química", "nota": 7.8},
    {"nombre": "Pedro", "edad": 22, "curso": "Matemáticas", "nota": 6.5},
    {"nombre": "Luisa", "edad": 20, "curso": "Física", "nota": 9.0},
])

# 2. Encontrar estudiantes con nota mayor a 8
estudiantes_nota_mayor_8 = estudiantes.find({"nota": {"$gt": 8}})
print("Estudiantes con nota mayor a 8:")
for estudiante in estudiantes_nota_mayor_8:
    print(estudiante)

# 3. Encontrar estudiantes de 20 años
estudiantes_20_años = estudiantes.find({"edad": 20})
print("\nEstudiantes de 20 años:")
for estudiante in estudiantes_20_años:
    print(estudiante)

# 4. Actualizar la nota de "Ana" a 9.5
estudiantes.update_one({"nombre": "Ana"}, {"$set": {"nota": 9.5}})

# 5. Incrementar la edad de todos los estudiantes en 1 año
estudiantes.update_many({}, {"$inc": {"edad": 1}})

# 6. Encontrar estudiantes con nota entre 7 y 9 y menos de 22 años
estudiantes_filtrados = estudiantes.find({
    "nota": {"$gte": 7, "$lte": 9},
    "edad": {"$lt": 22},
})
print("\nEstudiantes con nota entre 7 y 9 y menos de 22 años:")
for estudiante in estudiantes_filtrados:
    print(estudiante)

# 7. Calcular el promedio de las notas
promedio_notas = estudiantes.aggregate([{"$group": {"_id": None, "promedio": {"$avg": "$nota"}}}])
promedio = list(promedio_notas)[0]["promedio"]
print(f"\nPromedio de notas: {promedio}")

# 8. Agrupar por curso y calcular el promedio por curso
promedio_por_curso = estudiantes.aggregate([
    {"$group": {"_id": "$curso", "promedio": {"$avg": "$nota"}}}
])
print("\nPromedio de notas por curso:")
for curso in promedio_por_curso:
    print(f"Curso: {curso['_id']}, Promedio: {curso['promedio']}")

# 9. Crear un índice en el campo "curso"
estudiantes.create_index("curso")
print("\nÍndice creado en el campo 'curso'")

# 10. Consulta que utiliza el índice
estudiantes_matematicas = estudiantes.find({"curso": "Matemáticas"})
print("\nEstudiantes de Matemáticas (usando el índice):")
for estudiante in estudiantes_matematicas:
    print(estudiante)

# 11. Eliminar estudiantes con nota menor a 6
estudiantes.delete_many({"nota": {"$lt": 6}})
print("\nEstudiantes con nota menor a 6 eliminados.")

# 12. Crear la colección "cursos"
cursos = db["cursos"]

# Insertar documentos en la colección "cursos"
cursos.insert_many([
    {"nombre": "Matemáticas", "estudiantes": ["Ana", "Pedro"]},
    {"nombre": "Física", "estudiantes": ["Juan", "Luisa"]},
    {"nombre": "Química", "estudiantes": ["María"]},
])

# 13. Encontrar cursos en los que está inscrito un estudiante específico
estudiante_buscar = "Juan"
cursos_inscritos = cursos.find({"estudiantes": estudiante_buscar})
print(f"\nCursos en los que está inscrito {estudiante_buscar}:")
for curso in cursos_inscritos:
    print(curso["nombre"])

# Cerrar la conexión
client.close()