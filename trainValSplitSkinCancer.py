# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 23:15:02 2022

@author: Nikhil Sreedhar
"""

import os
import shutil
import random

path = os.getcwd()
vapath = 'val'
d1path = os.path.join(path, vapath)
if not os.path.isdir(d1path):
    os.makedirs(d1path)
    valAnom = os.makedirs(os.path.join(d1path, 'malignant'))
    valNorm = os.makedirs(os.path.join(d1path, 'benign'))


source =  (path+'/train/malignant')
target = (path+'/val/malignant')
files = os.listdir(source)
no_of_files = len(files) // 5

for file_name in random.sample(files, no_of_files):
    shutil.move(os.path.join(source, file_name), target)
        
source2 =  (path+'/train/benign')
target2 = (path+'/val/benign')
files2 = os.listdir(source2)
no_of_files2 = len(files2) // 5

for file_name2 in random.sample(files2, no_of_files2):
    shutil.move(os.path.join(source2, file_name2), target2)