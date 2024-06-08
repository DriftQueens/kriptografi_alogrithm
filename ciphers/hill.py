import numpy as np

# Membuat matriks kunci dari string kunci
def create_key_matrix(key):
    key = key.upper().replace(' ', '')
    size = int(len(key) ** 0.5)
    if size * size != len(key):
        raise ValueError("Panjang kunci harus merupakan kuadrat sempurna")
    key_matrix = np.array([ord(char) - ord('A') for char in key]).reshape(size, size)
    return key_matrix

# Mengonversi teks menjadi angka (A=0, B=1, ..., Z=25)
def text_to_numbers(text):
    return [ord(char) - ord('A') for char in text.upper().replace(' ', '')]

# Mengonversi angka kembali menjadi teks
def numbers_to_text(numbers):
    return ''.join(chr(num + ord('A')) for num in numbers)

# Menghitung invers modular dari sebuah bilangan
def mod_inv(a, m):
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"Tidak ada invers modular untuk {a} dalam modulus {m}")

# Menghitung invers modular dari matriks
def matrix_mod_inv(matrix, modulus):
    det = int(round(np.linalg.det(matrix)))  # Determinan matriks
    det_inv = mod_inv(det % modulus, modulus)  # Invers modular dari determinan
    matrix_minor = np.linalg.inv(matrix).T * det  # Matriks minor, ditranspos dan diskalakan dengan determinan
    adjugate = np.round(matrix_minor).astype(int) % modulus  # Matriks adjugate mod modulus
    return (det_inv * adjugate) % modulus

# Enkripsi menggunakan Hill Cipher
def encrypt(text, key='GYBNQKURP'):
    key_matrix = create_key_matrix(key)
    text_numbers = text_to_numbers(text)
    size = key_matrix.shape[0]
    padded_text = text_numbers + [0] * ((size - len(text_numbers) % size) % size)
    text_matrix = np.array(padded_text).reshape(-1, size)
    encrypted_matrix = np.dot(text_matrix, key_matrix) % 26
    encrypted_numbers = encrypted_matrix.flatten()
    return numbers_to_text(encrypted_numbers)

# Dekripsi menggunakan Hill Cipher
def decrypt(text, key='GYBNQKURP'):
    key_matrix = create_key_matrix(key)
    inverse_key_matrix = matrix_mod_inv(key_matrix, 26)
    text_numbers = text_to_numbers(text)
    size = key_matrix.shape[0]
    padded_text = text_numbers + [0] * ((size - len(text_numbers) % size) % size)
    text_matrix = np.array(padded_text).reshape(-1, size)
    decrypted_matrix = np.dot(text_matrix, inverse_key_matrix) % 26
    decrypted_numbers = decrypted_matrix.flatten()
    return numbers_to_text(decrypted_numbers)

