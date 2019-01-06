#!/usr/bin/env python3
#coding: utf-8

'''
根据关键词将文本分割，并保存为单独的文件.
usage:运行脚本，依次输入待分割文件->分割关键词->输出文件名
Author@LiYihang
<liyihang@shu.edu.cn>
'''

import re
import linecache
import pandas as pd

def fileParse():
    inputFile = input('Input SourcFile:')
    fp = open(inputFile, 'r')

    _cell_length_a = []
    _cell_length_b = []
    _cell_length_c = []
    _cell_angle_alpha = []
    _cell_angle_beta = []
    _cell_angle_gamma = []
    _symmetry_Int_Tables_number = []
    _symmetry_space_group_name_ = []
    _symmetry_cell_setting = []
    _pauling_file_object_repr = []
    _pauling_file_object_version = []
    _pauling_file_entry = []
    _pauling_file_entry_reference = []
    _pauling_file_phase = []
    _pauling_file_phase_reference = []

    dataInfo = ['_cell_length_a','_cell_length_b','_cell_length_c',
            '_cell_angle_alpha','_cell_angle_beta','_cell_angle_gamma',
            '_symmetry_Int_Tables_number','_symmetry_space_group_name_',
            '_symmetry_cell_setting','_pauling_file_object_repr',
            '_pauling_file_entry','_pauling_file_phase',
            '_pauling_file_entry_reference','_pauling_file_phase_reference']

    for eachLine in fp:
        eachLine = eachLine.strip('\n')

        if re.search('_cell_length_a', eachLine) is not None:
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

        elif re.search('_symmetry_Int_Tables_number', eachLine) is not None:
            number = re.compile(r'(_symmetry_Int_Tables_number)\s+(\d+)').search(eachLine)
            _symmetry_Int_Tables_number.append(number.group(2))

        elif re.search('_symmetry_space_group_name_H-M', eachLine) is not None:
            space_group_name = re.compile(r'(_symmetry_space_group_name_H-M)\s(.*)').search(eachLine)
            _symmetry_space_group_name_.append(space_group_name.group(2))

        elif re.search('_symmetry_cell_setting', eachLine) is not None:
            cell_setting = re.compile(r'(_symmetry_cell_setting)\s+(\w+)').search(eachLine)
            _symmetry_cell_setting.append(cell_setting.group(2))

        elif re.search('_pauling_file_object_repr', eachLine) is not None:
            repr = re.compile(r'(_pauling_file_object_repr)\s+(.*)').search(eachLine)
            _pauling_file_object_repr.append(repr.group(2))

        elif re.search('_pauling_file_entry ', eachLine) is not None:
            entry = re.compile(r'(_pauling_file_entry)\s+(.*)').search(eachLine)
            _pauling_file_entry.append(entry.group(2))

        elif re.search('_pauling_file_phase ', eachLine) is not None:
            phase = re.compile(r'(_pauling_file_phase)\s+(.*)').search(eachLine)
            _pauling_file_phase.append(phase.group(2))

        elif re.search('_pauling_file_entry_reference', eachLine) is not None:
            entry_reference = re.compile(r'(_pauling_file_entry_reference)\s+(.*)').search(eachLine)
            _pauling_file_entry_reference.append(entry_reference.group(2))

        elif re.search('_pauling_file_phase_reference', eachLine) is not None:
            phase_reference = re.compile(r'(_pauling_file_phase_reference)\s+(.*)').search(eachLine)
            _pauling_file_phase_reference.append(phase_reference.group(2))

        else:
            continue

    fp.close()

    df = pd.DataFrame({'_cell_length_a':pd.Series(_cell_length_a),
                        '_cell_length_b':pd.Series(_cell_length_b),
                        '_cell_length_c':pd.Series(_cell_length_c),
                        '_cell_angle_alpha':pd.Series(_cell_angle_alpha),
                        '_cell_angle_beta':_cell_angle_beta,
                        '_cell_angle_gamma':_cell_angle_gamma,
                        '_symmetry_Int_Tables_number':pd.Series(_symmetry_Int_Tables_number),
                       '_symmetry_space_group_name_':pd.Series(_symmetry_space_group_name_),
                       '_symmetry_cell_setting':pd.Series(_symmetry_cell_setting),
                       '_pauling_file_object_repr':pd.Series(_pauling_file_object_repr),
                       '_pauling_file_entry':pd.Series(_pauling_file_entry),
                       '_pauling_file_phase':pd.Series(_pauling_file_phase),
                       '_pauling_file_entry_reference':pd.Series(_pauling_file_entry_reference),
                       '_pauling_file_phase_reference':pd.Series(_pauling_file_phase_reference)})
    df.to_excel('spinel0.xlsx', sheet_name='cif', na_rep="NULL")


if __name__ == "__main__":
    fileParse()
