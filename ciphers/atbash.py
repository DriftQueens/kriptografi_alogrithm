def encrypt(text):
    def atbash_char(c):
        if 'A' <= c <= 'Z':
            return chr(ord('Z') - (ord(c) - ord('A')))
        elif 'a' <= c <= 'z':
            return chr(ord('z') - (ord(c) - ord('a')))
        else:
            return c

    return ''.join(atbash_char(c) for c in text)

def decrypt(text):
    return encrypt(text)


