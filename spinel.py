import pandas as pd

elements = ['Li', 'Be', 'Na', 'Mg', 'K', 'Ca', 'Sc', 'Ti', 'V', 'Cr',
            'Mn', 'Fe', 'Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Rb', 'Sr', 'Y',
            'Zr', 'Nb', 'Mo', 'Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In',
            'Sn', 'Cs', 'Ba', 'Hf', 'Ta', 'W', 'Re', 'Os', 'Ir', 'Pt',
            'Au', 'Hg', 'Tl', 'Pb', 'Bi','Fr', 'La', 'Ce', 'Pr', 'Nd',
            'Sm', 'Eu', 'Gd', 'Tb', 'Dy', 'Ho', 'Er', 'Tm', 'Yb', 'Lu',
            'Th', 'Pa',]

spinel_Z = []
spinel_F = []
for i in elements:
    for j in elements:
        if i != j:
            spinel_Z.append(i+j+str(2)+'O4')
        # spinel_F.append()
df = pd.DataFrame(spinel_Z)
df.to_excel('123spinel.xlsx', sheet_name='cif', header=['spinel'], na_rep="NULL")