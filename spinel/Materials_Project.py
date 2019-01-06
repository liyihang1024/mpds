# -*- coding: utf-8 -*-
import os
import pandas as pd

fileName = []
def file_name(file_dir):
    for root, dirs, files in os.walk(file_dir):
        print(root) #当前目录路径
        print(dirs) #当前路径下所有子目录
        print(files) #当前路径下所有非目录子文件
        for f in files:
            shotname, extension = os.path.splitext(f)
            fileName.append(shotname)

    df = pd.DataFrame(fileName)
    df.to_excel('spinel_update.xlsx', sheet_name='Materials_Project', index=False, header=['Structure'], na_rep="NULL")

file_name('Materials_Project_cif_update')
