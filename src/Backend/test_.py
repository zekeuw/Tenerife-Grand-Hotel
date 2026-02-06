import os
import pytest
import pymongo
from pymongo import MongoClient
import datetime


# -------------- backend files -------------------

from src.Backend.Connection import conectUsersCollection, conectBookingCollection, conectRoomCollection
from src.Backend.UsersManagement import createUser, logIn, updateUser, deleteUser
from src.Backend.Utils.Validations import retrieveUser
from src.Backend.BookingManagement import createBooking, UpdateBooking, GetAvailableRooms, GetBookingsOfUser, DeleteBookings

#------------------- Exceptions ---------------------
from pymongo.errors import DuplicateKeyError
from Utils.Exceptions import NotFoundError

@pytest.fixture
def cleanup_test_data():
    '''Cleanses the database for elements we are gonna use for the test'''
    yield 
    
    try:
        deleteUser("TESTUser")
    except:
        pass
    
    try:
        
        DeleteBookings("PR_1", "1920-05-04")
        DeleteBookings("PR_1", "1920-05-05")
        DeleteBookings("PR_1", "1920-05-07")
    except:
        pass


def test_duplicatedUsers():
    '''Checks if you can make duplicated users'''

    try:
        createUser({"username": "TESTUser", "password": "TESTUser", "name": "Test", "surname": "user", "phone": "123456789", "birth": "1924-05-12"})

        with pytest.raises(DuplicateKeyError):
            createUser({"username": "TESTUser", "password": "TESTUser", "name": "Test", "surname": "user", "phone": "123456789", "birth": "1924-05-12"})

    finally:
        deleteUser("TESTUser")

def test_canLogInAfterPassChange():
    '''Checks the passwords update correctly'''

    createUser({"username": "TESTUser", "password": "TESTUser", "name": "Test", "surname": "user", "phone": "123456789", "birth": "1924-05-12"})

    updateUser("TESTUser", None, "NewPass", None, None, None, None)

    log = logIn("TESTUser", "NewPass")

    deleteUser("TESTUser")

    assert log

def test_cantLogInDeletedUser():
    '''Creates a user, deletes it and then it tries to log in again'''

    createUser({"username": "TESTUser", "password": "TESTUser", "name": "Test", "surname": "user", "phone": "123456789", "birth": "1924-05-12"})

    deleteUser("TESTUser")

    
    log = logIn("TESTUser", "NewPass")

    assert not log

def test_cantOverlapBookings():
    '''Tries to create two bookings that overlap themselves'''
    try:
        createUser({"username": "TESTUser", "password": "TESTUser", "name": "Test", "surname": "user", "phone": "123456789", "birth": "1924-05-12"})

        createBooking("PR_1", "1920-05-05", "1920-05-06", "TESTUser")

        with pytest.raises(ValueError):
            createBooking("PR_1", "1920-05-04", "1920-05-07", "TESTUser")

    finally:
        deleteUser("TESTUser")
        DeleteBookings("PR_1", "1920-05-05")

def test_canCreateBookingAfterDelete():
    '''Creates a booking at one time, deletes it and checks that you can create a new booking'''

    try:
        createUser({"username": "TESTUser", "password": "TESTUser", "name": "Test", "surname": "user", "phone": "123456789", "birth": "1924-05-12"})

        createBooking("PR_1", "1920-05-05", "1920-05-06", "TESTUser")

        DeleteBookings("PR_1", "1920-05-05")
        
        createBooking("PR_1", "1920-05-04", "1920-05-07", "TESTUser")

        data = GetBookingsOfUser("TESTUser")

        assert data != []

    finally:
        DeleteBookings("PR_1", "1920-05-04")
        deleteUser("TESTUser")

def test_cantUpdateIntoUnavailableRoom():
    '''Tries to update a booking on a way it overlaps with another'''
    try:
        createUser({"username": "TESTUser", "password": "TESTUser", "name": "Test", "surname": "user", "phone": "123456789", "birth": "1924-05-12"})

        createBooking("PR_1", "1920-05-05", "1920-05-06", "TESTUser")
        
        createBooking("PR_1", "1920-05-07", "1920-05-09", "TESTUser")

        with pytest.raises(ValueError):
            UpdateBooking("PR_1", "1920-05-07", "1920-05-04", None)

    finally:
        DeleteBookings("PR_1", "1920-05-05")
        DeleteBookings("PR_1", "1920-05-07")
        deleteUser("TESTUser")
