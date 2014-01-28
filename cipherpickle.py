#!/bin/env python

import sys
import os
import base64

try:
    import cPickle as pickle
except:
    import pickle

import cipherlib

def dumps(obj, key):
    return cipherlib.encrypt(pickle.dumps(obj), key)

def loads(encrypted, key):
    return pickle.loads(cipherlib.decrypt(encrypted, key))

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

def main():
    test()

if __name__ == '__main__':
    main()
