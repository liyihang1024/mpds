#!/usr/bin/env python3
#coding: utf-8

'''
根据关键词将文本分割，并保存为单独的文件.
usage:运行脚本，依次输入待分割文件->分割关键词->输出文件名
Li Yihang <liyihang@shu.edu.cn>
'''

import re
import linecache
import pandas as pd

def fileParse():
    inputFile = input('Input SourcFile:')
    fp = open(inputFile, 'r')

    _chemical_formula_sum = []
    _cell_length_a = []
    _cell_length_b = []
    _cell_length_c = []
    _cell_angle_alpha = []
    _cell_angle_beta = []
    _cell_angle_gamma = []
    _cell_volume = []
    _exptl_crystal_density_diffrn = []
    _symmetry_space_group_name_ = []


    dataInfo = ['_chemical_formula_sum','_cell_length_a','_cell_length_b','_cell_length_c',
            '_cell_angle_alpha','_cell_angle_beta','_cell_angle_gamma','_cell_volume',
            '_exptl_crystal_density_diffrn','_symmetry_space_group_name_']

    for eachLine in fp:
        eachLine = eachLine.strip('\n')

        if re.search('_chemical_formula_sum', eachLine) is not None:
            formula = re.compile(r"(_chemical_formula_sum)\s+'(.*)'").search(eachLine)
            _cell_length_a.append(formula.group(2))

        elif re.search('_cell_length_a', eachLine) is not None:
            a = re.compile(r'(_cell_length_a)\s+(.*)').search(eachLine)
            _cell_length_a.append(a.group(2))

        elif re.search('_cell_length_b', eachLine) is not None:
            b = re.compile(r'(_cell_length_b)\s+(.*)').search(eachLine)
            _cell_length_b.append(b.group(2))

        elif re.search('_cell_length_c', eachLine) is not None:
            c = re.compile(r'(_cell_length_c)\s+(.*)').search(eachLine)
            _cell_length_c.append(c.group(2))

        elif re.search('_cell_angle_alpha', eachLine) is not None:
            alpha = re.compile(r'(_cell_angle_alpha)\s+(.*)').search(eachLine)
            _cell_angle_alpha.append(alpha.group(2))

        elif re.search('_cell_angle_beta', eachLine) is not None:
            beta = re.compile(r'(_cell_angle_beta)\s+(.*)').search(eachLine)
            _cell_angle_beta.append(beta.group(2))

        elif re.search('_cell_angle_gamma', eachLine) is not None:
            gamma = re.compile(r'(_cell_angle_gamma)\s+(.*)').search(eachLine)
            _cell_angle_gamma.append(gamma.group(2))

        elif re.search('_cell_volume', eachLine) is not None:
            volum = re.compile(r'(_cell_volume)\s+(\d+)').search(eachLine)
            _cell_volume.append(volum.group(2))

        elif re.search('_exptl_crystal_density_diffrn', eachLine) is not None:
            diffrn = re.compile(r'(_exptl_crystal_density_diffrn)\s(.*)').search(eachLine)
            _exptl_crystal_density_diffrn.append(diffrn.group(2))

        elif re.search('_symmetry_space_group_name_H-M', eachLine) is not None:
            space_group_name = re.compile(r'(_symmetry_space_group_name_H-M)\s(.*)').search(eachLine)
            _symmetry_space_group_name_.append(space_group_name.group(2))

        else:
            continue

    fp.close()

    df = pd.DataFrame({'_chemical_formula_sum':pd.Series(_chemical_formula_sum),
                       '_cell_length_a':pd.Series(_cell_length_a),
                        '_cell_length_b':pd.Series(_cell_length_b),
                        '_cell_length_c':pd.Series(_cell_length_c),
                        '_cell_angle_alpha':pd.Series(_cell_angle_alpha),
                        '_cell_angle_beta':pd.Series(_cell_angle_beta),
                        '_cell_angle_gamma':pd.Series(_cell_angle_gamma),
                       '_cell_volume':pd.Series(_cell_volume),
                        '_exptl_crystal_density_diffrn':pd.Series(_exptl_crystal_density_diffrn),
                       '_symmetry_space_group_name_':pd.Series(_symmetry_space_group_name_)})
    df.to_excel('spinel0.xlsx', sheet_name='cif', na_rep="NULL")


if __name__ == "__main__":
    fileParse()
