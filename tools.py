from datetime import datetime
import random
import string

def get_current_year():

    return datetime.now().year


def get_randnum():
    """
    Genera una cadena aleatoria de 9 dígitos para asignar como ID a cada estación climática

    """
    randnum = "".join(random.choices(string.digits, k=9))

    return randnum
