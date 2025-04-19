#utils.py

import os

def abs_path(ruta_relativa):

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_dir, ruta_relativa)
