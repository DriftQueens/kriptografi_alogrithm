def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('Modular inverse tidak ada')
    else:
        return x % m

def encrypt(plain_text):
    key = (5, 8)  # Kunci yang ditetapkan
    a, b = key
    result = ""
    for char in plain_text:
        if char.isalpha():
            if char.islower():
                result += chr(((a * (ord(char) - ord('a')) + b) % 26) + ord('a'))
            else:
                result += chr(((a * (ord(char) - ord('A')) + b) % 26) + ord('A'))
        else:
            result += char
    return result

def decrypt(cipher_text):
    key = (5, 8)  # Kunci yang ditetapkan
    a, b = key
    result = ""
    a_inv = modinv(a, 26)
    for char in cipher_text:
        if char.isalpha():
            if char.islower():
                result += chr(((a_inv * (ord(char) - ord('a') - b)) % 26) + ord('a'))
            else:
                result += chr(((a_inv * (ord(char) - ord('A') - b)) % 26) + ord('A'))
        else:
            result += char
    return result
