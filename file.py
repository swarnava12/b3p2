#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 16:37:24 2019

@author: pankaz-lab-pc3
"""

from rdkit import Chem
from rdkit.Chem import PandasTools
import pandas as pd
import os
from rdkit import RDConfig
from mordred import Calculator, descriptors
import pandas as pd
from sys import argv
filename = argv
txt = open(filename)
print(f"Heres your file{filename}:")
