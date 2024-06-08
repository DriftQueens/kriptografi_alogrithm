import math

def Enkripsi(plain_text, key):
    if len(key) <= len(plain_text) and len(key) > 1:
        jumlah_kolom = len(key)
        jumlah_baris = math.ceil(len(plain_text) / jumlah_kolom)
        key_generate = list(index for index, value in sorted(list(enumerate(key)), key= lambda x: x[1]))

        cipher_text = []

        # Loop melalui setiap indeks dalam list `indices`
        for index in key_generate:
            print("index = ", index)
            for i in range(jumlah_baris):
                # Tambahkan elemen pada indeks saat ini
                if index < len(plain_text):
                    cipher_text.append(plain_text[index])
                    print(index)
                    index += len(key_generate)

        return ''.join(cipher_text)
    else :
        return "key atau plaintext yang anda masukan tidak memenuhi syarat"

def Dekripsi(cipher_text, key):
    panjang_cipher_text = len(cipher_text)
    if len(key) <= panjang_cipher_text and len(key) > 1:
        jumlah_kolom = len(key)
        jumlah_baris = math.ceil(panjang_cipher_text/ jumlah_kolom)
        key_generate = [index for index, value in sorted(list(enumerate(key)), key=lambda x: x[1])]

        plain_text = [''] * panjang_cipher_text

        index = 0
        for col in key_generate:
            pos = col
            for row in range(jumlah_baris):
                if pos < panjang_cipher_text:
                    plain_text[pos] = cipher_text[index]
                    pos += jumlah_kolom
                    index += 1

        return ''.join(plain_text)
    else :
        return "key atau cipher text yang anda masukan tidak memenuhi syarat"
