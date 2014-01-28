#!/bin/env python

import ciphersaber
import StringIO
import base64

__n_default = 20 

def encrypt(plain_text, key, n=__n_default):
    fin = StringIO.StringIO(plain_text)
    fout = StringIO.StringIO()

    ciphersaber.process(True, fin, key, n, fout)
    return base64.standard_b64encode(fout.getvalue())

def decrypt(encrypted_text, key, n=__n_default):
    fin = StringIO.StringIO(base64.standard_b64decode(encrypted_text))
    fout = StringIO.StringIO()

    ciphersaber.process(False, fin, key, n, fout)
    return fout.getvalue()

def test():

    texts = [['Cipher Saver', '123456'],
             ['Test Test Test', 'qwe'], ]

    for text, key in texts:
        assert decrypt(encrypt(text,key),key) == text, 'Failed to encrypt/decrypt.' 

if __name__ == '__main__':
    test()
