#!/bin/env python

import ciphersaber
import StringIO

__n_default = 20 

def encrypt(plain_text, key, n=__n_default):
    fin = StringIO.StringIO(plain_text)
    fout = StringIO.StringIO()
    ciphersaber.process(True, fin, key, n, fout)
    return fout.getvalue()

def decrypt(encrypted_text, key, n=__n_default):
    fin = StringIO.StringIO(encrypted_text)
    fout = StringIO.StringIO()
    ciphersaber.process(False, fin, key, n, fout)
    return fout.getvalue()

def main():

    texts = [['Cipher Saver', '123456'],
             ['Test Test Test', 'qwe'], ]

    for text, key in texts:
        print 'plain:', text,
        encrypted = encrypt(text,key)
        decrypted = decrypt(encrypted, key)
        assert text == decrypted, 'Failed to encrypt/decrypt.' 
        print ' --> PASS'

if __name__ == '__main__':
    main()
