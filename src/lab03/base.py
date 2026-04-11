import sys
import os

# Define a raiz 'src' e adiciona lab01 e lab02 ao path
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab01'))
sys.path.insert(0, os.path.join(BASE_DIR, 'lab02'))

from model import Athlete
BaseAthlete = Athlete
