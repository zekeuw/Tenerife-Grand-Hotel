import pymongo
from pymongo import collection # para poner en la funcion que la variable tabla es una colección
from Connection import tablas, mydb

def Create(tabla: collection, datos: dict):
    tabla.InsertOne(datos)
