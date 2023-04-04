import h5py
import numpy as np
import os
from typing import Union

PATH = 'C:\\Users\\HPZ600intern1\\data'

def wrapper(func):
    def d_type(f_path):
        if not isinstance(f_path,str):
            raise TypeError
        func(f_path)
    
    return d_type

def wrapper_path(func):
    def file_exist(f_path):
        if os.path.exists(f_path) == False:
            raise OSError
        func(f_path)

    return file_exist

# @wrapper_path
# @wrapper
def read(
    f_path: str,
    row_idx: int,
    ) -> np.array: 

    with h5py.File(f_path, 'r') as f:
        #print("Klíče v souboru:", list(f.keys()))
        data = f['Data']                
        window_start = range(20, 41, 20)

        for index in window_start:
            yield data[row_idx, index-20:index]
            
        
               




def run():
    f_name = 'EB6_salb_1uM_(rec)_2020-11-09_14-39-51-073.h5'
    f_path = os.path.join(PATH, f_name)
    #f_path = 5
    data = read(f_path, row_idx=0)
    next(data)
    

if __name__ == '__main__':
    run()
