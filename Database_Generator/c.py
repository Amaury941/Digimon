import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv('digivolves_to.csv')

df.head()

from contextlib import redirect_stdout

with open('out1.txt', 'w') as f:
    with redirect_stdout(f):
        for mon in range(len(df[df.columns[0]])):
            print('CREATE EDGE Digivolves_to FROM (SELECT * FROM Digimon WHERE Name="%s") TO (SELECT * FROM Digimon WHERE Name="%s") SET Level=%s, Requires="%s"'
                %(
                    (df[df.columns[0]][mon]),
                    (df[df.columns[1]][mon]),
                    (df[df.columns[2]][mon]),
                    (df[df.columns[3]][mon]),
                )
            )