import pymongo
from ..Connection import contctUsersCollection

def retrieveUser(username: str):
    '''Busca al usuario por el username y devuelve el diccionario correspondiente'''
    '''A lo mejor deberia de haber un archivo distinto pa estas cosas'''

    users = contctUsersCollection()
    query = {"username": username}
    
    #deberia devolver una, que busca por el username
    data = users.find_one(query)

    return data
