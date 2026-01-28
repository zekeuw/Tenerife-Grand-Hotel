import pymongo
from pymongo import collection # para poner en la funcion que la variable tabla es una colección
from datetime import datetime
import bcrypt
import json

#----- Archivos propios -------
from Connection import conectUsersCollection
import Utils.Validations as Validations

#------ Errores --------
from pymongo.errors import DuplicateKeyError
from Utils.Exceptions import NotFoundError

'''Por ahora, de todo lo que hay creao solo esta testeado (y bastante pobremente además) el createUser y updateUser'''

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
    
    pass_bytes = data["password"].encode('utf-8')
    salt = bcrypt.gensalt()
    hash_bytes = bcrypt.hashpw(pass_bytes, salt)
    data["password"] = hash_bytes.decode('utf-8')

    #----------------------- Inserción -----------------------
    #conexión a la coleccion de la bd
    coll = conectUsersCollection()

    try:
        return coll.insert_one(data)
    except Exception as e:
        raise Exception("Error al insertar: ", e)

def logIn(username: str, password: str):
    '''Busca al usuario en la base de datos y comprueba que la contraseña sea correspondiente'''
    '''Devuelve True/False para confiramar el login (no creo q haga falta decir cual es cual)'''

    #pillamos los datos del usuario de la base de datos
    user = Validations.retrieveUser(username)

    if not user:
        # pa todas las paginas que alguna vez me han dicho "usuario o contraseña invalido" esta va pa ti
        # *ya he creado una excepcion llamada notFoundError pero por ahora se queda asi :D
        return False
    
    #bcrypt.verify devuelve true/false
    pass_bytes = password.encode('utf-8')
    db_hash = user["password"].encode('utf-8')

    return bcrypt.checkpw(pass_bytes, db_hash)

def updateUser(username, new_username, password, name, surname, phone, birth):
    '''Actualiza los usuarios con los datos puestos en los datos de arriba, username es para buscar el usuario, y new_username es el nuevo username'''
    '''Todos los datos salvo username pueden ser None, en caso de que lo sean no se actualizan.'''

    changes = {} #lista vacia que va a ir almacenando los cambios realizados

    users = conectUsersCollection()

    #recogemos todos los datos del usuario para reemplazar las variables que esten a None
    query = {"username": username}
    data = users.find_one(query)


    #---------------------------- Validaciones/datos sin cambiar ----------------------------------

    if data == None:
        raise NotFoundError("Usuario no encontrado.")

    if new_username != None:
        #comprobamos que el nombre de usuario no este en uso    
        if Validations.retrieveUser(new_username) != None:
            raise DuplicateKeyError("Nombre de usuario ya en uso.")
        changes["username"] = new_username
        
    if password != None:
        pass_bytes = password.encode('utf-8')
        hash_bytes = bcrypt.hashpw(pass_bytes, bcrypt.gensalt())
        changes["password"] = hash_bytes.decode('utf-8')

    if name != None:
        changes["name"] = name
    
    if surname != None:
        changes["surname"] = surname
    
    if phone != None:
        if not phone.isdigit() or len(phone) != 9:
            raise ValueError("El formato del teléfono no es válido")
        
        changes["phone"] = phone
    
    if birth != None:
        try:
            datetime.strptime(birth, "%Y-%m-%d")
            changes["birth"] = birth

        except ValueError:
            raise ValueError("Formato de fecha no válido")

    #------------------------------- Actualizacion ------------------------------

    filt = {'username': username}
    update = { '$set' :changes}
    
    users.update_one(filt, update)

def deleteUser(username):
    '''Vamos a confiar en el frontend para que nadie pueda borrar un usuario que no toca'''
    '''Y por cierto, la funcion borra usuarios :p'''

    user = Validations.retrieveUser(username)
    col = conectUsersCollection()

    if not user:
        raise NotFoundError("No se ha encontrado al usuario")
    
    query = {"username": username} #en tí confío pymongo
    col.delete_one(query)


def userSampleData():
    '''Crea un puñao de usuarios para la base de datos'''
    with open("./src/Backend/SampleData/Users.json", "r") as f:
        USERS = json.load(f)

        for user in USERS.values():

            try:
                createUser(user)

            except Exception as e:
                print(f"No se pudo insertar {user['username']}: {e}") #esta funcion es de debug asiq da un poco igual poner un print aqui


print(logIn("luis02", "passLuis02"))
# updateUser("luis01", None, None, "Pepito", "Perez", None, None) #testeo basico de update user