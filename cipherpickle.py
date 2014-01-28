#!/bin/env python

import StringIO
import base64

try:
    import cPickle as pickle
except:
    import pickle

import ciphersaber

__N_DEFAULT = 20

def encrypt(plain_text, key, n=__N_DEFAULT):
    fin = StringIO.StringIO(plain_text)
    fout = StringIO.StringIO()
    
    ciphersaber.process(True, fin, key, n, fout)
    return base64.standard_b64encode(fout.getvalue())


def decrypt(encrypted_text, key, n=__N_DEFAULT):
    fin = StringIO.StringIO(base64.standard_b64decode(encrypted_text))
    fout = StringIO.StringIO()

    ciphersaber.process(False, fin, key, n, fout)
    return fout.getvalue()

def dumps(obj, key):
    return encrypt(pickle.dumps(obj), key)

def loads(encrypted, key):
    return pickle.loads(decrypt(encrypted, key))

def test():
    obj = [[ i for i in range(50)],
           [ i*i for i in range(50)],
           [ i*i*i for i in range(50)],
           [ i*i*i*i for i in range(50)],
       ]
    key = 'secretkey'

    encrypted = dumps(obj,key)

    print obj
    print encrypted
    assert loads(encrypted,key) == obj

    texts = [['Cipher Saver', '123456'],
             ['Test Test Test', 'qwe'], ]

    for text, key in texts:
        assert decrypt(encrypt(text,key),key) == text, 'Failed to encrypt/decrypt.' 

def main():
    test()

if __name__ == '__main__':
    main()
