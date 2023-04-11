import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('database.csv')

df.head()

from contextlib import redirect_stdout

with open('out.txt', 'w') as f:
    with redirect_stdout(f):
        for mon in range(len(df[df.columns[0]])):
            print('CREATE VERTEX Digimon SET Name = "%s",Stage = "%s",Type = "%s",Attribute = "%s",Memory = %s,Equip_Slots = %s,HP = %s,SP = %s,Atk = %s,Def = %s,Int = %s,Spd = %s'
                %(
                (df[df.columns[0]][mon]),
                (df[df.columns[1]][mon]),
                (df[df.columns[2]][mon]),
                (df[df.columns[3]][mon]),
                (df[df.columns[4]][mon]),
                (df[df.columns[5]][mon]),
                (df[df.columns[6]][mon]),
                (df[df.columns[7]][mon]),
                (df[df.columns[8]][mon]),
                (df[df.columns[9]][mon]),
                (df[df.columns[10]][mon]),
                (df[df.columns[11]][mon]),
        ))
