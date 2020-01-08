import random
import struct
import json
import pickle

def save_text(file, data):
    with open(file, 'wt') as f:
        f.write(':'.join([str(v) for v in data]))

def load_text(file):
    with open(file) as f:
        return [float(x) for x in f.read().split(':')]

def save_bin(file, data):
    buff = bytearray(8)
    with open(file, 'wb') as f:
        for d in data:
            #print(d)
            struct.pack_into('d', buff, 0, d)
            f.write(buff)

def load_bin(file):
    data = []
    with open(file, 'rb') as f:
        while True:
            val = f.read(8)
            if val and len(val) == 8:
                fl = struct.unpack_from('d', val)[0]
                data.append(fl)
            else:
                break
        return data

def save_json(file, data):
    with open(file, 'wt') as f:
        json.dump(data, f)

def load_json(file):
    with open(file) as f:
        return json.load(f)

def save_pickle(file, data):
    with open(file, 'wb') as f:
        pickle.dump(data, f)
    
def load_pickle(file):
    with open(file, 'rb') as f:
        return pickle.load(f)
    
def gen_data(size):
    random.seed(1234)
    data = []
    for i in range(size):
        data.append(random.uniform(-100,100))
    else:
        return data
    
data = gen_data(10)
print(data)

tfile = './data.txt'
bfile = './data.bin'
pfile = './data.pkl'
jfile = './data.json'

print('\nText file: ')
save_text(tfile, data)
print(load_text(tfile))

print('\nBinary file: ')
save_bin(bfile, data)
print(load_bin(bfile))

print('\nPickle file: ')
save_pickle(pfile, data)
print(load_pickle(pfile))

print('\nJSON file: ')
save_json(jfile, data)
print(load_json(jfile))
