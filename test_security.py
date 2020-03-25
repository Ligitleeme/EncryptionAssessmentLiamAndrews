import Security
# Caesar pytest
def test_CaesarEncrypt_1():
    s = Security.Security()
    temp = s.CaesarEncrypt("c", "abc", 10)
    assert type(temp) == str

def test_CaesarEncrypt_2():
    s = Security.Security()
    temp = s.CaesarEncrypt("c", "abc", 10)
    assert temp != "abc"

def test_CaesarDecrypt_1():
    s = Security.Security()
    temp = s.CaesarDecrypt("c", "abc", 10)
    assert type(temp) == str

def test_CaesarDecrypt_2():
    s = Security.Security()
    temp = s.CaesarDecrypt("c", "abc", 10)
    assert temp != "abc"



# Poly pytest
def test_PolyEncrypt_1():
    s = Security.Security()
    temp = s.PolySubEncryptor("c", "abc")
    assert type(temp) == str

def test_PolyEncrypt_2():
    s = Security.Security()
    temp = s.PolySubEncryptor("c", "abc")
    assert temp != "abc"

def test_PolyDecrypt_1():
    s = Security.Security()
    temp = s.PolySubDecryptor("c")
    assert type(temp) == str

def test_PolyDecrypt_2():
    s = Security.Security()
    temp = s.PolySubDecryptor("c")
    assert temp != "abc"