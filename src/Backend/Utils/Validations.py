import pymongo
from ..Connection import conectUsersCollection

def retrieveUser(username: str):
    '''Busca al usuario por el username y devuelve el diccionario correspondiente'''
    '''A lo mejor deberia de haber puesto esto dentro de userManagement'''

    users = conectUsersCollection()
    query = {"username": username}
    
    #deberia devolver una, que busca por el username
    data = users.find_one(query)

    return data
