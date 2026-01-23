import pymongo
from pymongo import collection # para poner en la funcion que la variable tabla es una colección
from datetime import datetime
from passlib.hash import bcrypt
import json

#----- Archivos propios -------
from Connection import mydb, contctBookingCollection, contctUsersCollection, contctRoomCollection
import Utils.Validations as Validations

#------ Errores --------
from pymongo.errors import DuplicateKeyError
from Utils.Exceptions import NotFoundError

def createUser(data: dict):
    '''Crea un nuevo usuario en la base de datos en funcion a los datos introducidos en "data".'''
    '''Aqui estoy asumieno que los datos entran en el formato para la bd, si no entran en dicho formato hay que hacer otra función que los transforme al formato'''
    '''Devuelve un insert one object, por si hace falta usarlo para validar cosas'''

    #----------------------- Validaciones -----------------------
    #si ya hay un usuario con ese username devolvemos error
    if Validations.retrieveUser(data["username"]):
        raise DuplicateKeyError("Username repetido")
    
    phone = str(data["phone"]) #el str() es para el isdigit() de abajo

    if not phone.isdigit() or len(phone) != 9:
        raise ValueError("El formato del teléfono no es válido")
    
    try:
        datetime.strptime(data["birth"], "%Y-%m-%d")
    except ValueError:
        raise ValueError("Formato de fecha no válido")
    
    #hasheamos la contraseña (creamos una copia pq no me fio de hacer contraseña = bcrypt.hash(contraseña))
    user_data = data.copy()
    user_data["password"] = bcrypt.hash(data["password"])

    #----------------------- Inserción -----------------------
    #conexión a la coleccion de la bd
    coll = contctUsersCollection()

    try:
        return coll.insert_one(user_data)
    except Exception as e:
        raise Exception("Error al insertar: ", e)

def logIn(username: str, password: str):
    '''Busca al usuario en la base de datos y comprueba que la contraseña sea correspondiente'''
    '''Devuelve True/False para confiramar el login (no creo q haga falta decir cual es cual)'''

    #pillamos los datos del usuario de la base de datos
    user = Validations.retrieveUser(username)

    if not user:
        return False
    
    #bcrypt.verify devuelve true/false
    return bcrypt.verify(password, user["password"])

def updateUser(username, new_username, password, name, surname, phone, birth):
    '''Actualiza los usuarios con los datos puestos en los datos de arriba, username es para buscar el usuario, y new_username es el nuevo username'''
    '''Todos los datos salvo username pueden ser None, en caso de que lo sean no se actualizan.'''


    '''################################################ importante cambiar esto a tener un diccionario y actualizarlo '''


    users = contctUsersCollection()

    #recogemos todos los datos del usuario para reemplazar las variables que esten a None
    query = {"username": username}
    data = users.find_one(query)


    #---------------------------- Validaciones/datos sin cambiar ----------------------------------

    if data == None:
        raise NotFoundError("Usuario no encontrado.")

    if new_username == None:
        new_username = data["username"]

    #comprobamos que el nombre de usuario no este en uso    
    elif Validations.retrieveUser(new_username) != None:
        raise DuplicateKeyError("Nombre de usuario ya en uso.")
        
    if password == None:
        password = data["password"]

    else:
        bufferPswd = password.copy()
        password = bcrypt.hash(bufferPswd)

    if name == None:
        name = data["name"]
    
    if surname == None:
        surname = data["surname"]
    
    if phone == None:
        phone = data["phone"]
    
    else:
        if not phone.isdigit() or len(phone) != 9:
            raise ValueError("El formato del teléfono no es válido")
    
    if birth == None:
        birth = data["birth"]
    
    else:
        try:
            datetime.strptime(data["birth"], "%Y-%m-%d")

        except ValueError:
            raise ValueError("Formato de fecha no válido")

    #------------------------------- Actualizacion ------------------------------

    newvalues = {""}
    


def sampleData():
    '''Crea un puñao de usuarios para la base de datos'''
    with open("./src/Backend/SampleData/Users.json", "r") as f:
        USERS = json.load(f)

        for user in USERS.values():

            try:
                createUser(user)

            except Exception as e:
                print(f"No se pudo insertar {user['username']}: {e}")

sampleData()




