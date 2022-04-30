# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 01:16:32 2022

@author: Nikhil Sreedhar
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 23:10:30 2022

@author: Nikhil Sreedhar
"""
import glob
import os
import shutil
import csv


path = 'train'
labels = ('Mild', 'Moderate', 'Severe', 'Proliferative')

def categorize(path):
    imgList = glob.glob(path+'/*')
    
    apath = 'anomaly'
    f1path = os.path.join(path, apath)
    if not os.path.isdir(f1path):
        os.makedirs(f1path)
    npath = 'normal'
    f2path = os.path.join(path, npath)
    if not os.path.isdir(f2path):
        os.makedirs(f2path)
    
    for img in range(len(imgList)):

            with open ('trainLabels.csv', 'rt') as file:
                reader = csv.reader(file)
                # labelFile = pd.read_csv(file)
                x = imgList[img].split('\\')[1].split('.')[0]
                # rx = trainlist[0].split('\\')[1].split('.')[0]
        
                for row in reader:
                    if x == row[0]:
                        print(row)
                        if row[1] != str(0):
                            print('Found image with {} diabetic retinopathy label. Moving to anomaly directory.'.format(labels[int(row[1])-1]))
                            shutil.move(imgList[img], path+'/anomaly')
                        else:
                            print('Found image with normal label. Moving to normal directory.')
                            shutil.move(imgList[img], path+'/normal')
                        
categorize(path)


