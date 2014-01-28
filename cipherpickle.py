#!/bin/env python

import sys
import os

try:
    import cPickle as pickle
except:
    import pickle

import cipherlib
    
def dump(obj, key, out_stream = sys.stdout):
    encrypted = dumps(obj, key)
    out_stream.write(encrypted)
    out_stream.flush()

def load(in_stream, key):
    return loads( in_stream.read(), key)

def dumps(obj, key):
    return cipherlib.encrypt(pickle.dumps(obj), key)

def loads(encrypted, key):
    return pickle.loads(cipherlib.decrypt(encrypted, key))

def test():
    obj = [[1,2],3]
    key = 'secretkey'

    assert loads(dumps(obj, key), key) == obj

    filename = 'rmok.txt'
    try:
        with open(filename, 'wb') as out_stream:
            dump(obj, key, out_stream)

        with open(filename, 'rb') as in_stream:
            assert load(in_stream, key) == obj
    finally:
        os.remove(filename)

def main():
    test()

if __name__ == '__main__':
    main()
