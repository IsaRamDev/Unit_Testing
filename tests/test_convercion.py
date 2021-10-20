from pylenium.driver import Pylenium
from converciones import convercion

def test():
    assert convercion(5,2)==101

def test1():
    assert convercion(5476,2)==1010101100100

def test2():
    assert convercion(5476,3)==21111211
    
def test3():
    assert convercion(5476,4)==1111210

def test4():
    assert convercion(5476,5)==133401
    
def test5():
    assert convercion(5476,6)==41204

def test6():
    assert convercion(5476,7)==21652
    
def test7():
    assert convercion(5476,8)==12544

def test8():
    assert convercion(5476,9)==7454

def test9():
    assert convercion(5476,12)=="3204"
    
def test10():
    assert convercion(5476,16)=="1564"

def test11():
    assert convercion(1357435416,12)=="31A728AA0"
    
def test12():
    assert convercion(3547654646985,16)=="33A00B1ECC9"