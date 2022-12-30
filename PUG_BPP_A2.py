import PUG_BPP_A2_Functions as func
import io
import pytest, unittest

def test_crearFichero():
    assert func.crearFichero("prueba") == True
    
def test_borrarFichero():
    assert func.deleteFile("prueba") == True
    
def test_suma():
    assert func.suma(2) == 2
