#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  6 16:05:44 2019

@author: pankaz-lab-pc3
"""
import os
#os.system("source activate my-rdkit-env")
import sys
from rdkit import Chem
#from rdkit.Chem import PandasTools
import pandas as pd
#import os
#from rdkit import RDConfig
from mordred import Calculator, descriptors
import json
#smile_code = input()
if(len(sys.argv)>1):
    smile_code = sys.argv[1]
    print(smile_code)
    
    calc = Calculator(descriptors, ignore_3D=True)
    mols = [Chem.MolFromSmiles(smi) for smi in [smile_code]]
    df_final = calc.pandas(mols)
    df_show = df_final[['nAcid', 'nBase', 'nAtom', 'nHeavyAtom', 'BalabanJ', 'nBonds', 'nBondsO', 'nBondsS', 'SZ', 'Sm', 'Sv', 'Sse', 'Spe', 'NsLi', 'NssBe', 'nHBAcc', 'nHBDon', 'Lipinski', 'GhoseFilter', 'apol', 'bpol', 'SLogP', 'SMR',  'Radius', 'Diameter', 'TopoShapeIndex', 'MW', 'AMW', 'Zagreb1', 'Zagreb2']]
    pd.set_option('display.width', 1613)
    pd.set_option('display.max_columns', 1613)
    print(df_show)
    df_show.to_html('BBB/main/out.html')

def call(smile_code):
    #print(smile_code)
    calc = Calculator(descriptors, ignore_3D=True)
    mols = [Chem.MolFromSmiles(smi) for smi in smile_code if not smi ==""]
    df_final = calc.pandas(mols)
    df_show = df_final[['nAcid', 'nBase', 'nAtom', 'nHeavyAtom', 'BalabanJ', 'nBonds', 'nBondsO', 'nBondsS', 'SZ', 'Sm', 'Sv', 'Sse', 'Spe', 'NsLi', 'NssBe', 'nHBAcc', 'nHBDon', 'Lipinski', 'GhoseFilter', 'apol', 'bpol', 'SLogP', 'SMR',  'Radius', 'Diameter', 'TopoShapeIndex', 'MW', 'AMW', 'Zagreb1', 'Zagreb2']]
    pd.set_option('display.width', 1613)
    pd.set_option('display.max_columns', 1613)
    dfJson=json.loads(df_show.to_json(orient='records'))
    return dfJson
