import sys
import os

# Caminho para a pasta 'src'
BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

# Removemos qualquer referência errada ao lab02 no que toca a modelos
lab01_path = os.path.join(BASE_DIR, 'lab01')

# Forçamos o lab01 a ser o primeiro sítio onde o Python procura 'model'
if lab01_path not in sys.path:
    sys.path.insert(0, lab01_path)

from model import Athlete
BaseAthlete = Athlete
