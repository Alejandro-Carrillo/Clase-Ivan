from pymongo import MongoClient
from bson import ObjectId
import time

def imprimir_separador(titulo):
  print("\n" + "=" * 50) #\
  print(titulo)
  print("=" * 50)

# CONECTAR A MONGODB
try:
  cliente = MongoClient("mongodb://localhost:27012/")
  db = cliente["TiendaVirtual"]
  print("Conexion exitosa a MongoDB")
except Exception as e:
  print(f"rror al conectar a MongoDB: {e}")
  exit(1)

# CREAR COLECCION

productos = db["productos"]
pedidos = db["pedidos"]
detalles_pedido = ["detalles_pedido"]

# LIMPIAR COLECCIONES PARA LA DEMOSTRACION

productos.delete_many({})
pedidos.delete_many({})
detalles_pedido.delete_many({})

# 1. INSERTAR UN DOCUMENTO

imprimir_separador("1. Insertar un documento")
doc = {
  "nombre": "Regadera",
  "precio": 12000,
  "stock": 10
}
resultado = productos.insert_one(doc)
print(f"ID del documento insertado: {resultado.inserted_id}")

# 2. INSERTAR MULTIPLES DOCUMENTOS
imprimir_separador("2. Insertar multiples documentos")
nuevos_productos = [
  {"nombre": "Tijera", "precio": 8000, "stock": 15},
  {"nombre": "Maceta", "precio": 15000, "stock": 20}
]
resultado = productos.insert_many(nuevos_productos)
print(f"IDs de todos los documentos: {resultado.inserted_ids}")

# 3. CONSULTAR TODOS LOS DOCUMENTOS
imprimir_separador("3. Consultar todos los documentos")
for producto in productos.find():
  print(producto)

# 4. COSULTAR CON FILTRO
imprimir_separador("4 Consultar un productos con precio mayor a 10000")
for producto in productos.find({"precio": {"$gt": 10000}}):
  print(producto)
  
# 5. CONSULTAR UN SOLO DOCUMENTO
imprimir_separador("5. Consultar un producto especifico")
for producto in productos.find({"nombre": "Maceta"}):
  print(producto)

# 6. ACTUALIZAR UN DOCUMENTO
imprimir_separador("6. Actualizar un documento")
productos.update_one(
  {"nombre":"Tijera"},
  {"$set": {"precio": 8500}}
)
print("Producto actualizado: ")
print(productos.find_one({"nombre": "Tijera"}))

# 7. ACTUALIZAR VARIOS DOCUMENTOS
imprimir_separador("7. Actualizar varios documentos")
productos.update_many(
  {},
  {"$set": {"disponible": True}}
)
print(f"Cantidad de documentos actualizados: {resultado.modified_count}")

# 8. CONTAR DOCUMENTOS
imprimir_separador("8. Contar documentos")
total = productos.count_documents({})
print(f"Total de productos en la base de datos: {total}")

# 9. ORDENAR RASULTADOS
imprimir_separador("9. Productos ordenados por precio descendiente")
for producto in productos.find().sort("precio", -1):
  print(producto)
  
# 10. LIMITAR RESULTADOS
imprimir_separador("10. Primeros 2 productos")
for producto in productos.find().limit(2):
  print(producto)
  
# 11. CREAR INDICE
imprimir_separador("11. Crear indice")
indice = productos.create_index("nombre")
print(f"Indice creado: {indice}")

# 12. AGREGACION
imprimir_separador("12. Agregacion - Productos por rango de precio")
pipeline=[
  {
    "$group":{
      "_id":{
        "$switch":{
          "branches":[
            {"case":{"$lt":["$precio", 10000]}, "then": "Económico"},
            {"case":{"$lt":["$precio", 15000]}, "then": "Medio"}
          ],
          "default": "Premium"
        }
      },
      "cantidad": {"$sum": 1},
      "precio_promedio": {"$avg": "$precio"}
    }
  }
]
for resultado in productos.aggregate(pipeline):
  print(resultado)


# 13. AGREGACION
imprimir_separador("13. Ejemplo de $lookup (union de colecciones)")
pedido_id = pedidos.insert_one({
    "fecha": "2024-01-20",
    "cliente": "Cliente Ejemplo"
}).inserted_id

detalles_pedido.insert_many([
    {"pedidoId": pedido_id, "producto": "Regadera", "cantidad": 1},
    {"pedidoId": pedido_id, "producto": "Maceta", "cantidad": 2}
])

pipeline = [
    {
        "$lookup": {
            "from": "detalles_pedido",
            "localField": "_id",
            "foreignField": "pedidoId",
            "as": "detalles"
        }
    }
]
for pedido in pedidos.aggregate(pipeline):
    print("Pedidos completo con sus detalles:")
    print(pedido)

imprimir_separador("14. Eliminar documento")
resultado = productos.delete_one({"nombre": "Tijera"})
print(f"Cantidad de documentos eliminados: {resultado.deleted_count}")

cliente.close()
print("\nDemostracion completada. Conexion cerrada")

















