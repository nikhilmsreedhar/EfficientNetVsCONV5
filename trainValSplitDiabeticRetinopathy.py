import os
import shutil
import random

path = os.getcwd()
vapath = 'val'
d1path = os.path.join(path, vapath)
if not os.path.isdir(d1path):
    os.makedirs(d1path)
    valAnom = os.makedirs(os.path.join(d1path, 'anomaly'))
    valNorm = os.makedirs(os.path.join(d1path, 'normal'))


source =  (path+'/train/anomaly')
target = (path+'/val/anomaly')
files = os.listdir(source)
no_of_files = len(files) // 5

for file_name in random.sample(files, no_of_files):
    shutil.move(os.path.join(source, file_name), target)
        
source2 =  (path+'/train/normal')
target2 = (path+'/val/normal')
files2 = os.listdir(source2)
no_of_files2 = len(files2) // 5

for file_name2 in random.sample(files2, no_of_files2):
    shutil.move(os.path.join(source2, file_name2), target2)
