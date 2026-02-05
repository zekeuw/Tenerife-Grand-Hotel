import os
import pytest
import pymongo
import datetime


# -------------- backend files -------------------

from src.Backend.Connection import conectUsersCollection, conectBookingCollection, conectRoomCollection
from src.Backend.UsersManagement import createUser, logIn, updateUser, deleteUser
from src.Backend.Utils.Validations import retrieveUser
from src.Backend.BookingManagement import createBooking, UpdateBooking, GetAvailableRooms, GetBookingsOfUser

