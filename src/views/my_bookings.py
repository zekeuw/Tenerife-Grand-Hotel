import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

import flet as ft
from src.components.navigation_bar import NavigationBar

from src.Backend.BookingManagement import GetBookingsOfUser

