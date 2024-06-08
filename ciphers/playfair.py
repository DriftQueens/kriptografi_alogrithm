def create_playfair_matrix(key):
    key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
    key += ''.join(chr(i) for i in range(ord('A'), ord('Z') + 1) if chr(i) not in key and chr(i) != 'J')
    matrix = [key[i:i+5] for i in range(0, 25, 5)]
    return matrix

def encrypt_pair(pair, matrix):
    loc = {matrix[row][col]: (row, col) for row in range(5) for col in range(5)}
    a, b = pair
    row1, col1 = loc[a]
    row2, col2 = loc[b]
    if row1 == row2:
        return matrix[row1][(col1 + 1) % 5] + matrix[row2][(col2 + 1) % 5]
    elif col1 == col2:
        return matrix[(row1 + 1) % 5][col1] + matrix[(row2 + 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def decrypt_pair(pair, matrix):
    loc = {matrix[row][col]: (row, col) for row in range(5) for col in range(5)}
    a, b = pair
    row1, col1 = loc[a]
    row2, col2 = loc[b]
    if row1 == row2:
        return matrix[row1][(col1 - 1) % 5] + matrix[row2][(col2 - 1) % 5]
    elif col1 == col2:
        return matrix[(row1 - 1) % 5][col1] + matrix[(row2 - 1) % 5][col2]
    else:
        return matrix[row1][col2] + matrix[row2][col1]

def preprocess(text):
    text = text.upper().replace('J', 'I')
    pairs = []
    i = 0
    while i < len(text):
        a = text[i]
        b = text[i + 1] if i + 1 < len(text) else 'X'
        if a == b:
            pairs.append(a + 'X')
            i += 1
        else:
            pairs.append(a + b)
            i += 2
    return pairs

def encrypt(text, key='KEYWORD'):
    matrix = create_playfair_matrix(key)
    pairs = preprocess(text)
    return ''.join(encrypt_pair(pair, matrix) for pair in pairs)

def decrypt(text, key='KEYWORD'):
    matrix = create_playfair_matrix(key)
    pairs = preprocess(text)
    return ''.join(decrypt_pair(pair, matrix) for pair in pairs)
